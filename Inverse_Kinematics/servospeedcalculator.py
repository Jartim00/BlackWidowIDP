#!/usr/bin/python
import math
from ax import Ax12
ax = Ax12()
# max angle per second = 1.614 / 1024
def calculateTime(total_angle,speed):
	return (float(total_angle) * (1.614 / 1024.0)) * (float(speed) / 512.0)

def speedPerSec(time,total_angle):
	return float(time) / float(total_angle)

def calculateSpeed(total_angle,time):
	return (float(total_angle) / (float(time) / (1.614 / 1024.0))) * 512.0

def getSpeed(id,endPos,time):
	speed = 512
	if endPos > 1024 or endPos < 0:
		raise IndexError("End position out of bounds")
	curPos = ax.readPosition(id)
	totalAngle = math.fabs(curPos - endPos)
	speed = calculateSpeed(totalAngle, time)
	if speed > 512:
		raise Exception("Time is to low")
	return int(speed)
'''
   Moves the servo to the endPos in the specified time.
'''
def moveInTime(id,endPos,time):
	speed = 512
	try:
		speed = getSpeed(id,endPos,time)
	except:
		raise
	ax.moveSpeed(id,endPos,speed)

'''
   Sets servo action for moving to the endPos given the time.
   Execute ax.action() for actually moving the servo.
'''
def moveInTimeRW(id,endPos,time):
	speed = 512
	try:
		speed = getSpeed(id,endPos,time)
	except:
		raise
	ax.moveSpeedRW(id,endPos,speed)

if __name__ == "__main__":
	moveInTimeRW(13,500,1)
