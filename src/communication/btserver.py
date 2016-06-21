#!/usr/bin/python
import bluetooth
import subprocess
import json
from vision.vision import Vision
import threading
from movement.stab import Stabby
import movement.movement as movement
import movement.carry as carry
import gyro
mv = movement.Movement()

stab = Stabby()

## Bluetooth server for communication with the controller.
class BluetoothServer(object):

	#  @param bind_address The hexapod bluetooth address. Leave empty for letting anyone in.
	#  @param port The port for the socket
	#  @param mainprogram The mainprogram for setting main variables and calling main functions
	def __init__(self,bind_address,port,mainprogram):
		print "init"
		self.bind_address = bind_address
		self.port = port
		self.mainprogram = mainprogram
		self.server_sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
		self.running = False
		#make threads
		self.visionDetection = Vision()
		self.visionLineThread = threading.Thread(target=self.visionDetection.startAutonomousLine)
		self.visionBalloonThread = threading.Thread(target=self.visionDetection.startAutonomousBalloon)
		self.client_sock,self.address = (None,None)

	## Starts the bluetooth server
	def start(self):
		print "started"
		self.running = True
		#change the bind address when ready
		self.server_sock.bind((self.bind_address,self.port))
		self.server_sock.listen(1)
		#make server discoverable
		subprocess.call(['sudo', 'hciconfig', 'hci0', 'piscan'])
		self.acceptClient()
		self.communicate()

	## Stops the bluetooth server
	def stop(self):
		try:
			if self.client_sock is not None:
				self.client_sock.shutdown(1)
				self.client_sock.close()
		except:
			print "something went wrong when shutting down :("
		self.server_sock.shutdown(1)
		self.server_sock.close()
		self.running = False
		print "stopped"

	## Receive message from the client
	def receive(self,buf=1024,blocking=True):
		if not blocking:
			self.client_sock.settimeout(3.0)
		try:
			#receive
			data = self.client_sock.recv(buf)
			return data
		except bluetooth.btcommon.BluetoothError as e:
			# if blocking:
			raise e

	## Sends a string to the client
	#  @param msg The string to send
	def send(self, msg):
		try:
			#send
			self.client_sock.send(msg)
		except bluetooth.btcommon.BluetoothError as e:
			# if blocking:
			raise e

	## Communication between the server and client.
	#  Parses JSON and executes commands.
	#  Sends something back if needed.
	def communicate(self):
		print "communicate"
		while self.running:
			data = ""
			try:
				data = self.receive(1024,False)
				if data is None or data == "":
					continue
			except bluetooth.btcommon.BluetoothError as e:
				try:
					mv.rest()
				except:
					pass
				print "connection reset"
				#if lost connection, accept connecion for reconnect
				#set timeout
				self.acceptClient(False)
				continue
			try:
				jsonData = json.loads(data)
				self.parseJSON(jsonData)
				#self.client_sock.send(statuscode)#TODO
			except Exception,e :
				#send something back if something goes wrong
				print "Parsing JSON went wrong...", e
				#self.client_sock.send("-1")

	## Accepts a client.
	#  @param blocking when True, the function will wait till accepting a client.
	#  When False, the socket will wait 3 seconds.
	def acceptClient(self, blocking=True):
		if not blocking:
			self.server_sock.settimeout(3.0)
		try:
			self.client_sock,self.address = self.server_sock.accept()
			print "Accepted connection from ",self.address
		except bluetooth.btcommon.BluetoothError as e:
			if blocking:
				raise e
		# finally:
		# 	if blocking:
		# 		self.server_sock.settimeout(None)

	## Things that need to be stopped before doing another action.
	def stopEverything(self):
		self.stopVision()

	## Stops the balloon and line detection
	def stopVision(self):
		print "stopAutonomous"
		self.visionDetection.stopAutonomous()
		print "join thread"
		if self.visionLineThread.isAlive():
			self.visionLineThread.join()
		print "join last thread"
		if self.visionBalloonThread.isAlive():
			self.visionBalloonThread.join()

	## Returns  a JSON string with the battery status
	#  @param batteryStatus the battery status from 0 through 4
	def getBatteryJSON(self,batteryStatus):
		battery_json = {
			'cmd': 'setBattery',
			'battery_status' : batteryStatus
		}
		return json.dumps(battery_json, separators=(',',':'))

	## Parses JSON from the client and executes commands.
	#  Sends something back if needed.
	def parseJSON(self,jsonData):
		print jsonData
		if 'mode' in jsonData:
			#The command sets a mode
			mode = jsonData['mode']
			if mode == 1:
				#move mode
				if 'joy_pos' in jsonData:
					joy_pos = jsonData['joy_pos']
					if len(joy_pos) == 2:
						joy_x = joy_pos[0]
						joy_y = joy_pos[1]
						self.mainprogram.setJoyPos(joy_pos)
						#call the move function
						try:
							mv.movementController(joy_x,joy_y)
						except:
							print "error in movement"
			elif mode == 2:
				if 'danceId' in jsonData:
					danceId = jsonData['danceId']
					self.stopEverything()
					#call the dance function
					#TODO
					print "dance"
			elif mode == 3:
				#stop everything???
				self.stopEverything()
				#call the attack mode function
				stab.setAttackMode()
				stab.setStabPos()
				print "attack mode"
			elif mode == 4:
				#call the autonomousLine function
				print "autonomousLine"
				self.stopEverything()
				self.visionLineThread = threading.Thread(target=self.visionDetection.startAutonomousLine)
				self.visionLineThread.start()
			elif mode == 5:
				# call the autonomousBalloon function
				print "autonomousBalloon"
				self.stopEverything()
				self.visionBalloonThread = threading.Thread(target=self.visionDetection.startAutonomousBalloon)
				self.visionBalloonThread.start()
			elif mode == 6:
				self.stopEverything()
				# go to sleep
				print "go to sleep"
				mv.rest()
		elif 'cmd' in jsonData:
			cmd = jsonData['cmd']
			if cmd == 'batteryStatus':
				#get batteryStatus and send it back
				batteryStatus = self.mainprogram.getBatteryStatus()
				battery_json = self.getBatteryJSON(batteryStatus)
				try:
					self.send(battery_json)
				except Exception, e:
					print "Sending battery failed: ",e
			elif cmd == 'setGyro':
				if 'gyro' in jsonData:
					#gyro position
					gyro_pos = jsonData['gyro'];
					print "set gyro position"
					#rotate around the x axis
					if len(gyro_pos) == 3:
						self.mainprogram.setControllerGyroPos(gyro_pos)
						stab.gyroSens(gyro_pos[1])
			elif cmd == 'stab':
				stab.stab()
				stab.returning()
