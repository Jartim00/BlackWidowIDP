#!/usr/bin/python
import math
from ax import Ax12
ax = Ax12()

##Calulculates the amount of time a certain move action takes
#@param total_angle the product of the total angle change which the servo has to make.
#@param speed The servo speed which the action will be taken
#@param Return The time amount the action will take. 
def calculateTime(total_angle,speed):
	return (float(total_angle) * (1.614 / 1024.0)) * (float(speed) / 512.0)

##Calculates servo speed from the given time and total_angle
#@param time The total time in seconds
#@param total_angle the product of the total angle change which the servo has to make.
#@param returns servo speed
def speedPerSec(time,total_angle):
	return float(time) / float(total_angle)

##Calculates servo speed from the given time and total_angle
#@param time The total time in seconds
#@param total_angle the product of the total angle change which the servo has to make.
#@param returns servo speed
def calculateSpeed(total_angle,time):
	return (float(total_angle) / (float(time) / (1.614 / 1024.0))) * 512.0

##Calculates servo speed from the given time and total_angle
#@param id the id of the specific servo
#@param endPos the end position of servo between 0 - 1023
#@param time the time in which this action needs to be taken in seconds
#@param Return the calculated servo speed
def getSpeed(id,endPos,time):
	speed = 512
	if endPos > 1024 or endPos < 0:
		raise IndexError("End position out of bounds")
	curPos = ax.readPosition(id)
	totalAngle = math.fabs(curPos - endPos)
	speed = calculateSpeed(totalAngle, time)
	if speed > 1023:
		e = "Time is too low! (" + str(int(speed)) + ")"
		raise Exception(e)
	return int(speed)

##Moves the servo to the endPos in the specified time.
#@param id the id of the specific servo
#@param endPos the end position of servo between 0 - 1023
#@param time the time in which this action needs to be taken in seconds 
def moveInTime(id,endPos,time):
	speed = 512
	try:
		speed = getSpeed(id,endPos,time)
	except:
		raise
	ax.moveSpeed(id,endPos,speed)

##Sets servo action for moving to the endPos given the time. Execute ax.action() for actually moving the servo.
#@param id the id of the specific servo
#@param endPos the end position of servo between 0 - 1023
#@param time the time in which this action needs to be taken in seconds 
def moveInTimeRW(id,endPos,time):
	speed = 512
	try:
		speed = getSpeed(id,endPos,time)
	except:
		raise
	ax.moveSpeedRW(id,endPos,speed)

if __name__ == "__main__":
	moveInTimeRW(13,500,1)
