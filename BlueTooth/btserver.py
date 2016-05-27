#!/usr/bin/python

import bluetooth
import subprocess

class BluetoothServer(object):
	def __init__(self):
		
server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 1
server_sock.bind(("",port))
server_sock.listen(1)
#make server discoverable
subprocess.call(['sudo', 'hciconfig', 'hci0', 'piscan'])
client_sock,address = server_sock.accept()
print "Accepted connection from ",address
try:
	while True:
		data = client_sock.recv(1024)
		print "received [%s]" % data
		client_sock.send(data)
except KeyboardInterrupt:
	client_sock.close()
	server_sock.close()
