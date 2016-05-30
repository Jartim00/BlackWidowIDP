#!/usr/bin/python
import bluetooth
import subprocess
import json
import vision.vision as vision

class BluetoothServer(object):
	def __init__(self,bind_address,port):
		print "init"
		self.bind_address = bind_address
		self.port = port
		self.server_sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
		self.running = False

	def start(self):
		print "started"
		self.running = True
		#change the bind address when ready
		self.server_sock.bind((self.bind_address,self.port))
		self.server_sock.listen(1)
		#make server discoverable
		subprocess.call(['sudo', 'hciconfig', 'hci0', 'piscan'])
		self.acceptClient(True)
		self.communicate()

	def stop(self):
		self.client_sock.shutdown(1)
		self.server_sock.shutdown(1)
		self.client_sock.close()
		self.server_sock.close()
		self.running = False
		print "stopped"

	def communicate(self):
		print "communicate"
		while self.running:
			data = ""
			try:
				print "receiving..."
				data = self.client_sock.recv(1024)
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

	def acceptClient(self, blocking):
		if not blocking:
			self.client_sock.settimeout(0)
		self.client_sock,self.address = self.server_sock.accept()
		print "Accepted connection from ",self.address

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
					print "move"
			elif mode == 2:
				if 'danceId' in jsonData:
					danceId = jsonData['danceId']
					#call the dance function
					print "dance"
			elif mode == 3:
				#call the stab function
				print "stab"
			elif mode == 4:
				#call the autonomousLine function
				print "autonomousLine"
			elif mode == 5:
				# call the autonomousBalloon function
				print "autonomousBalloon"
			elif mode == 6:
				# go to sleep
				print "go to sleep"
		elif 'client_sockcmd' in jsonData:
			cmd = jsonData['cmd']
			if cmd == 'batteryStatus':
				#get batteryStatus and send it back
				print "batteryStatus"
			elif cmd == 'setGyro':
				if 'gyro' in jsonData:
					#gyro position
					gyro_pos = jsonData['gyro'];
					print "set gyro position"
