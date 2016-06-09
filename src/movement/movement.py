#!/usr/bin/python
import math
from ax import Ax12
from time import sleep
import os

class movement:

    def rest(self, leg) :
            offset = 71
            loc = [0,0]
            if leg == 1 :
                loc = IK().calc_angles(0, 84.24478972, offset)
            elif leg == 2 :
                loc = IK().calc_angles(0, 103.1783, offset)
            elif leg == 3 :
                loc = IK().calc_angles(0, 84.24478972, offset)
            elif leg == 4 :
                loc = IK().calc_angles(0, 84.24478972, offset)
            elif leg == 5 :
                loc = IK().calc_angles(0, 103.1783, offset)
            elif leg == 6 :
                loc = IK().calc_angles(0, 84.24478972, offset)
            #ready positions
    	try:
    	        ax.moveSpeedRW(leg*10 + 1, 512, 450)
     	        ax.moveSpeedRW(leg*10 + 2, loc[0], 450)
       	        ax.moveSpeedRW(leg*10 + 3, loc[1], 450)
    		sleep(0.04)
    	except:
    		try:
    		        ax.moveSpeedRW(leg*10 + 1, 512, 450)
    	 	        ax.moveSpeedRW(leg*10 + 2, loc[0], 450)
    	   	        ax.moveSpeedRW(leg*10 + 3, loc[1], 450)
    			sleep(0.04)
    		except:
    			pass
            # TODO do this here?

    def raiselegs(self, leg):
    	l = (leg*10)+2
    	oldP = 700 + 50
    	ax.moveSpeedRW(l, int(oldP),350)
    	ax.action()
    	sleep(0.05)


    def lowerlegs(self, leg):
    	l = (leg*10)+2
    	oldP = 700 - 50
    	ax.moveSpeedRW(l, int(oldP),350)
    	ax.action()
    	sleep(0.05)


    def stapvooruit(self, leg, angle_modifier=0.0):
    	#print "Loss loss loss"
    	offset = 71
    	angle = 0
    	loc = [0,0]
    	if leg == 1 :
    		angle = 9.73 + angle_modifier
    		loc = IK().calc_angles(0, 84.24478972, offset)
    		#loc = IK().calc_angles( 119.1401242, 84.24478972, offset)
    	elif leg == 2 :
    		angle = 25 + angle_modifier
    		loc = IK().calc_angles(0, 103.1783, offset)
    		#loc = IK().calc_angles(119.1401242, 103.1783, offset)
    	elif leg == 3 :
    		angle = 45 + angle_modifier
    		loc = IK().calc_angles(0, 84.24478972, offset)
    		#loc = IK().calc_angles( 119.1401242, 84.24478972, offset)
    	elif leg == 4 :
    		angle = -45 + angle_modifier
    		loc = IK().calc_angles(0, 84.24478972, offset)
    		#loc = IK().calc_angles( 119.1401242, 84.24478972, offset)
    	elif leg == 5 :
    		angle = -25 + angle_modifier
    		loc = IK().calc_angles(0, 103.1783, offset)
    		#loc = IK().calc_angles(119.1401242, 103.1783, offset)
    	elif leg == 6 :
    		angle = -9.73 + angle_modifier
    		loc = IK().calc_angles(0, 84.24478972, offset)
    		#loc = IK().calc_angles( 119.1401242, 84.24478972, offset)
    	#ready positions
    	#print(leg*10 + 1, AngleToServo(angle), 300,leg*10 + 2, loc[0], 300,leg*10 + 3, loc[1], 300)
    	try:
    		ax.moveSpeedRW(leg*10 + 1, int(AngleToServo(angle)), 350)
    		#ax.moveSpeedRW(leg*10 + 2, int(loc[0]), 350)
    		ax.moveSpeedRW(leg*10 + 3, int(loc[1]), 350)
    	except:
    		try:
    			ax.moveSpeedRW(leg*10 + 1, int(AngleToServo(angle)), 350)
    			#ax.moveSpeedRW(leg*10 + 2, int(loc[0]), 350)
    			ax.moveSpeedRW(leg*10 + 3, int(loc[1]), 350)
    		except:
    			pass
    	#ax.action()
    	#sleep(0.1)
            # TODO do this here?

    def stapzuruck(self, leg,angle_modifier=0.0):
    	#print "zuruck"
    	offset = 71
    	angle = 0
    	loc = [0,0]
    	if leg == 1 :
    		angle = -45 + angle_modifier
    		loc = IK().calc_angles(0, 84.24478972, offset)
    		#loc = IK().calc_angles( 119.1401242, 84.24478972, offset)
    	elif leg == 2 :
    		angle = -25 + angle_modifier
    		loc = IK().calc_angles(0, 103.1783, offset)
    		#loc = IK().calc_angles(119.1401242, 103.1783, offset)
    	elif leg == 3 :
    		angle = -9.73 + angle_modifier
    		loc = IK().calc_angles(0, 84.24478972, offset)
    		#loc = IK().calc_angles( 119.1401242, 84.24478972, offset)
    	elif leg == 4 :
    		angle = 9.73 + angle_modifier
    		loc = IK().calc_angles(0, 84.24478972, offset)
    		#loc = IK().calc_angles( 119.1401242, 84.24478972, offset)
    	elif leg == 5 :
    		angle = 25 + angle_modifier
    		loc = IK().calc_angles(0, 103.1783, offset)
    		#loc = IK().calc_angles(119.1401242, 103.1783, offset)
    	elif leg == 6 :
    		angle = 45 + angle_modifier
    		loc = IK().calc_angles(0, 84.24478972, offset)
    		#loc = IK().calc_angles( 119.1401242, 84.24478972, offset)
    	#ready positions
    	#print(leg*10 + 1, AngleToServo(angle), 300,leg*10 + 2, loc[0], 300,leg*10 + 3, loc[1], 300)
    	try:
    		ax.moveSpeedRW(leg*10 + 1, int(AngleToServo(angle)), 350)
    		#ax.moveSpeedRW(leg*10 + 2, int(loc[0]), 350)
    		ax.moveSpeedRW(leg*10 + 3, int(loc[1]), 350)
    	except:
    		try:
    			ax.moveSpeedRW(leg*10 + 1, int(AngleToServo(angle)), 350)
    			#ax.moveSpeedRW(leg*10 + 2, int(loc[0]), 350)
    			ax.moveSpeedRW(leg*10 + 3, int(loc[1]), 350)
    		except:
    			pass

    def moveBackward(moveAngleLeft=0.0, moveAngleRight=0.0):
        for x in range(2, 7, 2):
            raiselegs(x)
        ax.action()
        sleep(0.005)
        for x in range(2, 7, 2):
            #stapvooruit(x,moveAngleLeft)#, 8.0
            stapzuruck(x, moveAngleLeft)
        ax.action()
        sleep(0.005)
        for x in range(2, 7, 2):
            lowerlegs(x)
        ax.action()
        sleep(0.005)
        for x in range(1, 7, 2):
            raiselegs(x)
        ax.action()
        sleep(0.005)
        for x in range(2, 7, 2):
            #stapzuruck(x)
            stapvooruit(x)
        ax.action()
        sleep(0.005)
        for x in range(1, 7, 2):
            #stapvooruit(x, moveAngleRight*-1)#, -8.0
            stapzuruck(x, moveAngleRight*-1)
        ax.action()
        sleep(0.005)
        for x in range(1, 7, 2):
            lowerlegs(x)
        ax.action()
        sleep(0.005)
        for x in range(2, 7, 2):
            raiselegs(x)
        ax.action()
        sleep(0.005)
        for x in range(1, 7, 2):
            #stapzuruck(x)
            stapvooruit(x)
        ax.action()
        sleep(0.005)

    def moveForward(moveAngleLeft=0, moveAngleRight=0):
        for x in range(2, 7, 2):
            raiselegs(x)
        ax.action()
        sleep(0.005)
        for x in range(2, 7, 2):
            stapvooruit(x,moveAngleLeft)#, 8.0
        ax.action()
        sleep(0.005)
        for x in range(2, 7, 2):
            lowerlegs(x)
        ax.action()
        sleep(0.005)
        for x in range(1, 7, 2):
            raiselegs(x)
        ax.action()
        sleep(0.005)
        for x in range(2, 7, 2):
            stapzuruck(x)
        ax.action()
        sleep(0.005)
        for x in range(1, 7, 2):
            stapvooruit(x, moveAngleRight*-1)#, -8.0
        ax.action()
        sleep(0.005)
        for x in range(1, 7, 2):
            lowerlegs(x)
        ax.action()
        sleep(0.005)
        for x in range(2, 7, 2):
            raiselegs(x)
        ax.action()
        sleep(0.005)
        for x in range(1, 7, 2):
            stapzuruck(x)
        ax.action()
        sleep(0.005)

    def turnLeft():
        pass

    def turnRigh():
        pass
