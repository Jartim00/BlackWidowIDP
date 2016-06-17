#!/usr/bin/python
import math
from ax import Ax12
from time import sleep
from kinematic import Kinematic
import os
import speedcalc
sCalc = Speedcalculation()
ax = Ax12()
bx = Kinematic()

class Bridge:
    isMoving = False
    ##Ready legs for Bridge
    def readyForBridge(self):
		isMoving = True
		loc = [0,0]
		for x in range(1,7):
			loc = bx.calc_angles(0, 84.24478972, 0)
			ax.moveSpeedRW(leg*10 + 2, loc[0], 450)
            ax.moveSpeedRW(leg*10 + 3, loc[1], 450)
			if leg == 2 or leg == 5:
				ax.moveSpeedRW(leg*10 + 1, 512, 450)
			elif leg ==  1 or leg == 4:
				ax.moveSpeedRW(leg*10 + 1, bx.AngleToServo(45), 450)
			else:
				ax.moveSpeedRW(leg*10 + 1, bx.AngleToServo(-45), 450)
		isMoving = False
	
	##Push the rear legs to slide across the bridge
	def pushBackLegs(self):
		isMoving = True
		loc = bx.calc_angles(0, 119.24478972, 5)
		#push legs
		for x in range(3,4):
			ax.moveSpeedRW(leg*10 + 2, loc[0], 450)
			ax.moveSpeedRW(leg*10 + 3, loc[1], 450)	
		sleep(0.1)
		#raise legs
		loc = bx.calc_angles(0, 84.24478972, 0)
		for x in range(3,4):
			ax.moveSpeedRW(leg*10 + 2, loc[0] + 50, 450)
			ax.moveSpeedRW(leg*10 + 3, loc[1], 450)
		sleep(0.1)
		#lower legs
        for x in range(3,4):
			ax.moveSpeedRW(leg*10 + 2, loc[0], 450)
			ax.moveSpeedRW(leg*10 + 3, loc[1], 450)
		sleep(0.1)
		isMoving = False
	
	##Pulls the front legs to slide across the bridge
	def pushFrontLegs(self):
		isMoving = True
		#raise legs
		loc = bx.calc_angles(0, 119.24478972, 0)
		for x in range(1,7,5):
			ax.moveSpeedRW(leg*10 + 2, loc[0] + 50, 450)
			ax.moveSpeedRW(leg*10 + 3, loc[1], 450)
		sleep(0.1)
		#lower legs
        for x in range(1,7,5):
			ax.moveSpeedRW(leg*10 + 2, loc[0], 450)
			ax.moveSpeedRW(leg*10 + 3, loc[1], 450)
		sleep(0.1)	
		#pull legs
		loc = bx.calc_angles(0, 84.24478972, 5)
		for x in range(1,7,5):
			ax.moveSpeedRW(leg*10 + 2, loc[0], 450)
			ax.moveSpeedRW(leg*10 + 3, loc[1], 450)	
		sleep(0.1)	
		isMoving = False