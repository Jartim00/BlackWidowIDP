#!/usr/bin/python
import math
from ax import Ax12
from time import sleep
from kinematic import Kinematic
import os
import speedcalc
ax = Ax12()
bx = Kinematic()

class Movement:
    isMoving = False
    ##Places a hexapod leg in rest position
    #@param leg Integer representing leg id ranges between 1 to 6
    def rest(self, leg) :
        offset = 71
        loc = [0,0]
        if leg == 1 :
            loc = bx.calc_angles(0, 84.24478972, offset)
        elif leg == 2 :
            loc = bx.calc_angles(0, 103.1783, offset)
        elif leg == 3 :
            loc = bx.calc_angles(0, 84.24478972, offset)
        elif leg == 4 :
            loc = bx.calc_angles(0, 84.24478972, offset)
        elif leg == 5 :
            loc = bx.calc_angles(0, 103.1783, offset)
        elif leg == 6 :
            loc = bx.calc_angles(0, 84.24478972, offset)
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

   ##Raises hexapod leg from the ground
   #@param leg Integer representing leg id ranges between 1 to 6
    def raiselegs(self, leg):
    	l = (leg*10)+2
    	oldP = 700 + 50
    	ax.moveSpeedRW(l, int(oldP),350)
    	ax.action()
    	sleep(0.05)

    ##Lowers hexapod leg from the ground
    #@param leg Integer representing leg id ranges between 1 to 6
    def lowerlegs(self, leg):
    	l = (leg*10)+2
    	oldP = 700 - 50
    	ax.moveSpeedRW(l, int(oldP),350)
    	ax.action()
    	sleep(0.05)

    ##Moves hexapod leg forward using inverse kinematics
    #@param leg Integer representing leg id ranges between 1 to 6
    #@param angle_modifier Float representing angle modifier used to change walking angle
    #@param gate_mod Float representing distance between body and length in millimeters
    def stapvooruit(self, leg, angle_modifier, gate_mod,speed):
    	#print "Loss loss loss"
    	offset = 71
    	angle = 0
    	loc = [0,0]
    	if leg == 1 :
    		angle = 9.73 + angle_modifier
    		#loc = IK().calc_angles(0, 84.24478972, offset)
    		loc = bx.calc_angles(119.1401242, 84.24478972 + gate_mod, offset)
    	elif leg == 2 :
    		angle = 25 + angle_modifier
    		loc = bx.calc_angles(0, 103.1783 + gate_mod, offset)
    		#loc = IK().calc_angles(119.1401242, 103.1783, offset)
    	elif leg == 3 :
    		angle = 45 + angle_modifier
    		loc = bx.calc_angles(0, 84.24478972 + gate_mod, offset)
    		#loc = IK().calc_angles( 119.1401242, 84.24478972, offset)
    	elif leg == 4 :
    		angle = -45 + angle_modifier
    		loc = bx.calc_angles(0, 84.24478972 + gate_mod, offset)
    		#loc = IK().calc_angles( 119.1401242, 84.24478972, offset)
    	elif leg == 5 :
    		angle = -25 + angle_modifier
    		loc = bx.calc_angles(0, 103.1783 + gate_mod, offset)
    		#loc = IK().calc_angles(119.1401242, 103.1783, offset)
    	elif leg == 6 :
    		angle = -9.73 + angle_modifier
    		#loc = IK().calc_angles(0, 84.24478972, offset)
    		loc = bx.calc_angles(119.1401242, 84.24478972 + gate_mod, offset)
    	#ready positions
    	#print(leg*10 + 1, AngleToServo(angle), 300,leg*10 + 2, loc[0], 300,leg*10 + 3, loc[1], 300)
    	try:
    		ax.moveSpeedRW(leg*10 + 1, int(bx.AngleToServo(angle)), speed)
    		#ax.moveSpeedRW(leg*10 + 2, int(loc[0]), 350)
    		ax.moveSpeedRW(leg*10 + 3, int(loc[1]), speed)
    	except:
    		try:
    			ax.moveSpeedRW(leg*10 + 1, int(bx.AngleToServo(angle)), speed)
    			#ax.moveSpeedRW(leg*10 + 2, int(loc[0]), 350)
    			ax.moveSpeedRW(leg*10 + 3, int(loc[1]), speed)
    		except:
    			pass

    ##Moves hexapod leg backward using inverse kinematics
    #@param leg Integer representing leg id ranges between 1 to 6
    #@param angle_modifier Float representing angle modifier used to change walking angle
    #@param gate_mod Float representing distance between body and length in millimeters
    def stapzuruck(self, leg,angle_modifier,gate_mod,speed):
    	#print "zuruck"
    	offset = 71
    	angle = 0
    	loc = [0,0]
    	if leg == 1 :
    		angle = -45 + angle_modifier
    		loc = bx.calc_angles(0, 84.24478972 + gate_mod, offset)
    		#loc = IK().calc_angles( 119.1401242, 84.24478972, offset)
    	elif leg == 2 :
    		angle = -25 + angle_modifier
    		loc = bx.calc_angles(0, 103.1783 + gate_mod, offset)
    		#loc = IK().calc_angles(119.1401242, 103.1783, offset)
    	elif leg == 3 :
    		angle = -9.73 + angle_modifier
    		#loc = IK().calc_angles(0, 84.24478972, offset)
    		loc = bx.calc_angles(119.1401242, 84.24478972 + gate_mod, offset)
    	elif leg == 4 :
    		angle = 9.73 + angle_modifier
    		#loc = IK().calc_angles(0, 84.24478972, offset)
    		loc = bx.calc_angles(119.1401242, 84.24478972 + gate_mod, offset)
    	elif leg == 5 :
    		angle = 25 + angle_modifier
    		loc = bx.calc_angles(0, 103.1783 + gate_mod, offset)
    		#loc = IK().calc_angles(119.1401242, 103.1783, offset)
    	elif leg == 6 :
    		angle = 45 + angle_modifier
    		loc = bx.calc_angles(0, 84.24478972 + gate_mod, offset)
    		#loc = IK().calc_angles( 119.1401242, 84.24478972, offset)
    	#ready positions
    	#print(leg*10 + 1, AngleToServo(angle), 300,leg*10 + 2, loc[0], 300,leg*10 + 3, loc[1], 300)

    	try:
    		ax.moveSpeedRW(leg*10 + 1, int(bx.AngleToServo(angle)), speed)
    		#ax.moveSpeedRW(leg*10 + 2, int(loc[0]), 350)
    		ax.moveSpeedRW(leg*10 + 3, int(loc[1]), speed)
    	except Exception, e:
		print e
    		try:
    			ax.moveSpeedRW(leg*10 + 1, int(bx.AngleToServo(angle)), speed)
    			#ax.moveSpeedRW(leg*10 + 2, int(loc[0]), 350)
    			ax.moveSpeedRW(leg*10 + 3, int(loc[1]), speed)
    		except Exception, e:
    			print "ex",e


    ##Moves the hexapod backward using inverse kinematics
    #@param moveAngleLeft Float representing angle modifier used to change walking angle to the left side
    #@param moveAngleRight Float representing angle modifier used to change walking angle to the right side
    #@param gate_mod Float representing distance between body and length in millimeters
    def moveBackward(self,moveAngleLeft, moveAngleRight,gate_mod,speed):
	Movement.isMoving = True
        for x in range(2, 7, 2):
            self.raiselegs(x)
        ax.action()
        sleep(0.05)
        for x in range(2, 7, 2):
            #stapvooruit(x,moveAngleLeft)#, 8.0
            self.stapzuruck(x, moveAngleLeft, gate_mod,speed)
        ax.action()
        sleep(0.05)
        for x in range(2, 7, 2):
            self.lowerlegs(x)
        ax.action()
        sleep(0.05)
        for x in range(1, 7, 2):
            self.raiselegs(x)
        ax.action()
        sleep(0.05)
        for x in range(2, 7, 2):
            #stapzuruck(x)
            self.stapvooruit(x,0, gate_mod,speed)
        ax.action()
        sleep(0.05)
        for x in range(1, 7, 2):
            #stapvooruit(x, moveAngleRight*-1)#, -8.0
            self.stapzuruck(x, moveAngleRight*-1, gate_mod,speed)
        ax.action()
        sleep(0.05)
        for x in range(1, 7, 2):
            self.lowerlegs(x)
        ax.action()
        sleep(0.05)
        for x in range(2, 7, 2):
            self.raiselegs(x)
        ax.action()
        sleep(0.05)
        for x in range(1, 7, 2):
            #stapzuruck(x)
            self.stapvooruit(x, 0,gate_mod,speed)
        ax.action()
        sleep(1)
	Movement.isMoving = False

    ##Moves the hexapod forward using inverse kinematics
    #@param moveAngleLeft Float representing angle modifier used to change walking angle to the left side
    #@param moveAngleRight Float representing angle modifier used to change walking angle to the right side
    #@param gate_mod Float representing distance between body and length in millimeters
    def moveForward(self,moveAngleLeft, moveAngleRight, gate_mod,speed):
	Movement.isMoving = True
        for x in range(2, 7, 2):
            self.raiselegs(x)
        ax.action()
        sleep(0.05)
        for x in range(2, 7, 2):
            self.stapvooruit(x,moveAngleLeft, gate_mod, speed)#, 8.0
        ax.action()
        sleep(0.05)
        for x in range(2, 7, 2):
            self.lowerlegs(x)
        ax.action()
        sleep(0.05)
        for x in range(1, 7, 2):
            self.raiselegs(x)
        ax.action()
        sleep(0.05)
        for x in range(2, 7, 2):
            self.stapzuruck(x,0,gate_mod,speed)
        ax.action()
        sleep(0.05)
        for x in range(1, 7, 2):
            self.stapvooruit(x, moveAngleRight*-1, gate_mod,speed)#, -8.0
        ax.action()
        sleep(0.05)
        for x in range(1, 7, 2):
            self.lowerlegs(x)
        ax.action()
        sleep(0.05)
        for x in range(2, 7, 2):
            self.raiselegs(x)
        ax.action()
        sleep(0.05)
        for x in range(1, 7, 2):
            self.stapzuruck(x,0, gate_mod,speed)
        ax.action()
        sleep(1)
	Movement.isMoving = False

	#turn per 45 degrees
    def turnLeft(self):
	Movement.isMoving = True
	speed = 300
    	#poot omhoog
    	ax.moveSpeedRW(12, 750, speed)
    	ax.moveSpeedRW(13, 880, speed)
    	ax.moveSpeedRW(32, 750, speed)
    	ax.moveSpeedRW(33, 880, speed)
    	ax.moveSpeedRW(52, 750, speed)
    	ax.moveSpeedRW(53, 880, speed)
    	ax.action()
    	sleep(0.05)

    	#draai
    	ax.moveSpeedRW(11, 358, speed)
    	ax.moveSpeedRW(31, 358, speed)
    	ax.moveSpeedRW(51, 400, speed)
    	ax.action()
    	sleep(0.05)

	#poot omlaag
	ax.moveSpeedRW(12, 620, speed)
	ax.moveSpeedRW(32, 620, speed)
	ax.moveSpeedRW(52, 620, speed)
	ax.action()
	sleep(0.05)

	#poot omhoog
	ax.moveSpeedRW(22, 750, speed)
	ax.moveSpeedRW(23, 880, speed)
	ax.moveSpeedRW(42, 750, speed)
	ax.moveSpeedRW(43, 880, speed)
	ax.moveSpeedRW(62, 750, speed)
	ax.moveSpeedRW(63, 880, speed)
	ax.action()
	sleep(0.05)

	#draai lichaam
	ax.moveSpeedRW(11, 512, speed)
	ax.moveSpeedRW(31, 512, speed)
	ax.moveSpeedRW(51, 512, speed)
	ax.action()
	sleep(0.05)

	ax.moveSpeedRW(21, 400, speed)
	ax.moveSpeedRW(41, 358, speed)
	ax.moveSpeedRW(61, 358, speed)
	ax.action()
	sleep(0.05)

	#poot omlaag
	ax.moveSpeedRW(22, 620, speed)
	ax.moveSpeedRW(42, 620, speed)
	ax.moveSpeedRW(62, 620, speed)
	ax.action()
	sleep(0.05)

	#poot omhoog
	ax.moveSpeedRW(12, 750, speed)
	ax.moveSpeedRW(13, 880, speed)
	ax.moveSpeedRW(32, 750, speed)
	ax.moveSpeedRW(33, 880, speed)
	ax.moveSpeedRW(52, 750, speed)
	ax.moveSpeedRW(53, 880, speed)
	ax.action()
	sleep(0.05)

	#draai lichaam
	ax.moveSpeedRW(21, 512, speed)
	ax.moveSpeedRW(41, 512, speed)
	ax.moveSpeedRW(61, 512, speed)
	ax.action()
	sleep(0.05)

	ax.moveSpeedRW(11, 358, speed)
	ax.moveSpeedRW(31, 358, speed)
	ax.moveSpeedRW(51, 400, speed)
	ax.action()
	sleep(1)
	Movement.isMoving = False
	#for x in range(1, 7):
	#	self.rest(x)

	#turn per 45 degrees
    def turnRight(self):
    	Movement.isMoving = True
    	speed = 300
        ax.moveSpeedRW(12, 750, speed)
        ax.moveSpeedRW(13, 880, speed)
        ax.moveSpeedRW(32, 750, speed)
        ax.moveSpeedRW(33, 880, speed)
        ax.moveSpeedRW(52, 750, speed)
        ax.moveSpeedRW(53, 880, speed)
        ax.action()
        sleep(0.05)

        #draai
        ax.moveSpeedRW(11, 666, speed)
        ax.moveSpeedRW(31, 666, speed)
        ax.moveSpeedRW(51, 600, speed)
        ax.action()
        sleep(0.05)

           #poot omlaag
    	ax.moveSpeedRW(12, 620, speed)
    	ax.moveSpeedRW(32, 620, speed)
    	ax.moveSpeedRW(52, 620, speed)
    	ax.action()
    	sleep(0.05)

    	#poot omhoog
    	ax.moveSpeedRW(22, 750, speed)
    	ax.moveSpeedRW(23, 880, speed)
    	ax.moveSpeedRW(42, 750, speed)
    	ax.moveSpeedRW(43, 880, speed)
    	ax.moveSpeedRW(62, 750, speed)
    	ax.moveSpeedRW(63, 880, speed)
    	ax.action()
    	sleep(0.05)

    	#draai lichaam
    	ax.moveSpeedRW(11, 512, speed)
    	ax.moveSpeedRW(31, 512, speed)
    	ax.moveSpeedRW(51, 512, speed)
    	ax.action()
    	sleep(0.05)

    	ax.moveSpeedRW(21, 600, speed)
    	ax.moveSpeedRW(41, 666, speed)
    	ax.moveSpeedRW(61, 666, speed)
    	ax.action()
    	sleep(0.05)

    	#poot omlaag
    	ax.moveSpeedRW(22, 620, speed)
    	ax.moveSpeedRW(42, 620, speed)
    	ax.moveSpeedRW(62, 620, speed)
    	ax.action()
    	sleep(0.05)

    	#poot omhoog
    	ax.moveSpeedRW(12, 750, speed)
    	ax.moveSpeedRW(13, 880, speed)
    	ax.moveSpeedRW(32, 750, speed)
    	ax.moveSpeedRW(33, 880, speed)
    	ax.moveSpeedRW(52, 750, speed)
    	ax.moveSpeedRW(53, 880, speed)
    	ax.action()
    	sleep(0.05)

    	#draai lichaam
    	ax.moveSpeedRW(21, 512, speed)
    	ax.moveSpeedRW(41, 512, speed)
    	ax.moveSpeedRW(61, 512, speed)
    	ax.action()
    	sleep(0.05)

    	ax.moveSpeedRW(11, 666, speed)
    	ax.moveSpeedRW(31, 666, speed)
    	ax.moveSpeedRW(51, 600, speed)
    	ax.action()
    	sleep(1)
    	Movement.isMoving = False
    	#for x in range(1, 7):
    	#	self.rest(x)


    def movementController(self,x,y):
        print "before check"
    	if Movement.isMoving:
    		return
        print "let's start moving"
	if x < 10 and x > -10:
		if y > 10:
			print "vooruit"
			self.moveForward(0,0,-20,int(speedcalc.speed(y)))
		elif y < 10:
			print "achteruit"
			self.moveBackward(0,0,-20,int(speedcalc.speed(y)))
	elif x <= -10:
		#if y >= 0:
		#	self.moveForward(x/10,0,0,int(speedcalc.speed(y)))
		#else:
		#	self.moveBackward(x/10,0,0,int(speedcalc.speed(y)))
		print "turnright"
		self.turnRight()
	elif x >= 10:
		#if y >= 0:
		#	self.moveForward(0,x/10,0,int(speedcalc.speed(y)))
		#else:
		#	self.moveBackward(0,x/10,0,int(speedcalc.speed(y)))
		print "turnleft"
		self.turnLeft()
	


    	"""if y >= 10:
	    print "forward"
    	    if x >= 10:
    		self.moveForward(0,x/10,0,int(speedcalc.speed(y)))
    	    elif x <= -10:
    		self.moveForward(x/10,0,0,int(speedcalc.speed(y)))
    	    else:
    		self.moveForward(0,0,0,int(speedcalc.speed(y)))
        elif y <= -10:
	    print "backward"
    	    if x >= 10:
    		self.moveBackward(0,x/10,0,int(speedcalc.speed(y)))
    	    elif x <= -10:
    		self.moveBackward(x/10,0,0,int(speedcalc.speed(y)))
    	    else:
    		self.moveBackward(0,0,0,int(speedcalc.speed(y)))
	elif y <= 10 and y >= -10:
	    print "neutral"
            if x >= 10:
		print "right"
    		self.turnRight()
            elif x <= -10:
		print "left"
                self.turnLeft()"""
	    
#try:
#	while True:
#		Movement().movementController(11.0,0.0)
#		#sleep(1)
#except KeyboardInterrupt:
#	for x in range(1, 7):
#    	    Movement().rest(x)
#            ax.action()
