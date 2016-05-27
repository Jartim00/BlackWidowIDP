#!/usr/bin/python

import bluetooth
import subprocess
import json
# class BluetoothServer(object):
# 	def __init__(self,):

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 1
#change the bind address when ready
server_sock.bind(("",port))
server_sock.listen(1)
#make server discoverable
subprocess.call(['sudo', 'hciconfig', 'hci0', 'piscan'])
client_sock,address = server_sock.accept()
print "Accepted connection from ",address
def parseJSON(jsonData):
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
try:
	while True:
		data = client_sock.recv(1024)
		print "received [%s]" % data
		# try:
		jsonData = json.loads(data)
		parseJSON(jsonData)
		# except:
		# 	#send something back if something goes wrong
		# 	print "SOMETHING WENT WRONG"
		client_sock.send(data)
except KeyboardInterrupt:
	client_sock.close()
	server_sock.close()
