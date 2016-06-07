#!/usr/bin/python
import bluetooth
import subprocess
import json
from vision.vision import Vision
import threading
from movement.vooruit import vooruit as movement
import gyro

class BluetoothServer(object):
	def __init__(self,bind_address,port):
		print "init"
		self.bind_address = bind_address
		self.port = port
		self.server_sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
		self.running = False
		#make threads
		self.visionDetection = Vision()
		self.visionLineThread = threading.Thread(target=self.visionDetection.startAutonomousLine)
		self.visionBalloonThread = threading.Thread(target=self.visionDetection.startAutonomousBalloon)

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

	def stop(self):
		self.client_sock.shutdown(1)
		self.server_sock.shutdown(1)
		self.client_sock.close()
		self.server_sock.close()
		self.running = False
		print "stopped"

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

	def communicate(self):
		print "communicate"
		while self.running:
			print "SELF.RUNNING : ",self.running
			data = ""
			try:
				print "receiving..."
				data = self.receive(1024,False)
				if data is None or data == "":
					continue
				print "end receive..."
			except bluetooth.btcommon.BluetoothError as e:
				print "connection reset"
				#if lost connection, accept connecion for reconnect
				#set timeout
				self.acceptClient(False)
				continue
			print "received [%s]" % data
			try:
				jsonData = json.loads(data)
				self.parseJSON(jsonData)
			except:
				#send something back if something goes wrong
				print "SOMETHING WENT WRONG"
			print "sending..."
			self.client_sock.send(data)

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
	def stopEverything(self):
		self.stopVision()

	def stopVision(self):
		print "stopAutonomous"
		self.visionDetection.stopAutonomous()
		print "join thread"
		if self.visionLineThread.isAlive():
			self.visionLineThread.join()
		print "join last thread"
		if self.visionBalloonThread.isAlive():
			self.visionBalloonThread.join()

	def parseJSON(self,jsonData):
		if 'mode' in jsonData:
			#The command sets a mode
			mode = jsonData['mode']
			if mode == 1:
				#move mode
				if 'joy_x' in jsonData and 'joy_y' in jsonData:
					joy_x = jsonData['joy_x']
					joy_y = jsonData['joy_y']
					#call the move function
					if joy_x > 0 and joy_y == 0:
						self.__SpiderAction('Right')
					elif joy_x < 0 and joy_y == 0:
						self.__SpiderAction('Left')
					elif joy_y > 0 and joy_x == 0:
						self.__SpiderAction('Forward')
					print "move"
			elif mode == 2:
				if 'danceId' in jsonData:
					danceId = jsonData['danceId']
					self.stopEverything()
					#call the dance function
					print "dance"
			elif mode == 3:
				#stop everything???
				self.stopEverything()
				#call the stab function
				print "stab"
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
		elif 'cmd' in jsonData:
			cmd = jsonData['cmd']
			if cmd == 'batteryStatus':
				#get batteryStatus and send it back
				print "batteryStatus"
			elif cmd == 'setGyro':
				if 'gyro' in jsonData:
					#gyro position
					gyro_pos = jsonData['gyro'];
					print "set gyro position"
					#rotate around the x axis
					gyro.gyroSens(gyro_pos[0])

	def __SpiderAction(self,command):
		print command
		if command == "Forward":
			movement().vooruit()
		elif command == "Left":
			movement().links()
		elif command == "Right":
			movement().rechts()
		movement().rust()
