#!/usr/bin/python
from ax import Ax12
from time import sleep
import os

ax = Ax12()
leg = 2
_HEUP = 10*leg+1
_KNIE = 10*leg+2
_VOET = 10*leg+3

print ax.readMovingStatus(_VOET)
print ax.readRWStatus(_VOET)

def prN(num):
	if(num < -100) :
		return str(num)
	elif(num < -10) :
		return str(num) + " "
	elif(num < 0) :
		return str(num) + "  "
	elif(num < 10):
		return str(num) + "   "
	elif(num <100):
		return str(num) + "  "
	elif(num<1000):
		return str(num) + " "
	else:
		return str(num)


while(True) :
	tempH = ax.readTemperature(_HEUP)
	tempK = ax.readTemperature(_KNIE)
	tempV = ax.readTemperature(_VOET)

	posiH = ax.readPosition(_HEUP)
	posiK = ax.readPosition(_KNIE)
	posiV = ax.readPosition(_VOET)

	voltH = ax.readVoltage(_HEUP)
	voltK = ax.readVoltage(_KNIE)
	voltV = ax.readVoltage(_VOET)

	loadH = ax.readLoad(_HEUP)
	loadK = ax.readLoad(_KNIE)
	loadV = ax.readLoad(_VOET)

	try:
		speeH = ax.readSpeed(_HEUP)
	except:
		speeH = "----"
	try:
		speeK = ax.readSpeed(_KNIE)
	except:
		speeK = "----"
	try:
		speeV = ax.readSpeed(_VOET)
	except:
		speeV = "----"

	os.system('clear')
	print ax.learnServos(10, 70) #min-ID, max-ID, verbose=False
	print " "
	print "     | HEUP | KNIE | VOET "
	print "=========================="
	print "pos  |", prN(posiH), "|", prN(posiK), "|", prN(posiV)
	print "temp |", prN(tempH), "|", prN(tempK), "|", prN(tempV)
	print "spd  |", prN(speeH), "|", prN(speeK), "|", prN(speeV)
	print "volt |", prN(voltH), "|", prN(voltK), "|", prN(voltV)
	print "load |", prN(loadH), "|", prN(loadK), "|", prN(loadV)

	sleep(0.5)
