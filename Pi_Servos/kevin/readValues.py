#!/usr/bin/python
from ax import Ax12
from time import sleep
import os, sys
ax = Ax12()

def prN(num): #print Number with indentation
	if(num < -100) :
		return str(num)
	elif(num < -10) :
		return str(num) + " "
	elif(num < 0) :
		return " " + str(num) + " "
	elif(num < 10):
		return " " + str(num) + "  "
	elif(num <100):
		return " " + str(num) + " "
	elif(num<1000):
		return str(num) + " "
	else:
		return str(num)

def speed(servo) :
	#speed is a bit tricky at times
	if ax.readMovingStatus(servo) : #alleen als er een commando gegeven is om te bewegen - niet als je 'm handmatig beweegt :(
		try:
			spd = ax.readSpeed(servo)
		except:
			spd = "----"
	else :
		spd = "----"
	return spd

def volt(servo) :
	#speed is a bit tricky at times
	try:
		volt = ax.readVoltage(servo)
		volt = str(volt/10) + "." + str(volt%10)
	except:
		volt = "----"
	return volt	

def readValues(delay=0.25) :
	#print table
	list = ax.learnServos(10,64) #min-ID, max-ID, verbose=False
	while screenRunning :
		try:
			sleep(delay)
			os.system('clear')
			print "     | pos  | temp | spd  | volt | load "
			print "========================================"
			for i in range(0, len(list)) :
				servo = list[i]	
				print prN(servo), "|", prN(ax.readPosition(servo)), "|", prN(ax.readTemperature(servo)), "|", prN(speed(servo)), "|", volt(servo), "|", prN(ax.readLoad(servo))
				if servo % 10 == 3 :
					print "" #extra newline
		except KeyboardInterrupt :
			print " Exited"
			sys.exit(0)

try :
	screenRunning = True
	readValues(0.25)
except KeyboardInterrupt :
	print " exit."