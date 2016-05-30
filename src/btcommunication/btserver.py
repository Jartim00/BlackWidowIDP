#!/usr/bin/python

import bluetooth
import subprocess
import json

class BluetoothServer(object):
	def __init__(self,bind_address,port):
		self.bind_address = bind_address
		self.port = port
		self.server_sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )

	def start(self):
		#change the bind address when ready
		self.server_sock.bind((self.bind_address,self.port))
		self.server_sock.listen(1)
		#make server discoverable
		subprocess.call(['sudo', 'hciconfig', 'hci0', 'piscan'])
		self.acceptClient()
		self.communicate()

	def communicate(self):
		try:
			while True:
				data = ""
				try:
					data = self.client_sock.recv(1024)
				except bluetooth.btcommon.BluetoothError as e:
					print "connection reset"
					#if lost connection, accept connecion for reconnect
					self.acceptClient()
					continue
				print "received [%s]" % data
				try:
					jsonData = json.loads(data)
					self.parseJSON(jsonData)
				except:
					#send something back if something goes wrong
					print "SOMETHING WENT WRONG"
				self.client_sock.send(data)
		except KeyboardInterrupt:
			self.client_sock.close()
			self.server_sock.close()

	def acceptClient(self):
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
