#!/usr/bin/python
from time import sleep
from ax import Ax12
ax = Ax12()

numLegs = 6
servosPerLeg = 3
speed = 350
#sets the spider to carry mode
def carry():
	for legNum in range(1,numLegs + 1):
 		for servoNum in range(1,servosPerLeg+1):
	     		servoId = legNum * 10 + servoNum
	     		print "servo: ", servoId
	     		if servoNum == 1:
				if legNum == 2 or legNum == 5:
					ax.moveSpeedRW(servoId,512,speed)
	     			elif legNum == 1 or legNum == 4:
					ax.moveSpeedRW(servoId,350,speed)
				elif legNum == 3 or legNum == 6:
					ax.moveSpeedRW(servoId,674,speed)
			elif servoNum == 2:
				ax.moveSpeedRW(servoId,820,speed)
	     		elif servoNum == 3:
				ax.moveSpeedRW(servoId,1020,speed)
	ax.action()
	sleep(0.5)

if __name__ == "__main__":
	carry()
