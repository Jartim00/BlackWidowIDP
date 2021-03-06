#!/usr/bin/python
import math
from ax import Ax12
from time import sleep
from kinematic import Kinematic
import os
from speedcalc import Speedcalculation
sCalc = Speedcalculation()
ax = Ax12()
bx = Kinematic()

class Movement:
    isMoving = False
    ##Places a hexapod leg in rest position
    #@param leg Integer representing leg id ranges between 1 to 6
    def restLeg(self, leg) :
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
            ax.moveSpeed(leg*10 + 1, 512, 450)
            ax.moveSpeed(leg*10 + 2, loc[0], 450)
            ax.moveSpeed(leg*10 + 3, loc[1], 450)
            #sleep(0.04)
        except:
            try:
                ax.moveSpeed(leg*10 + 1, 512, 450)
                ax.moveSpeed(leg*10 + 2, loc[0], 450)
                ax.moveSpeed(leg*10 + 3, loc[1], 450)
                #sleep(0.04)
            except:
    	       pass

    def rest(self):
	    for x in range(1, 7):
			self.restLeg(x)
            ax.action()

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
    #@param speed int representing speed between 0 and 1023
    def stapvooruit(self, leg, angle_modifier, gate_mod,speed):
    	#print "Loss loss loss"
    	offset = 71
    	angle = 0
    	loc = [0,0]
    	if leg == 1 :
    		angle = 9.73 + angle_modifier
    		#loc = IK().calc_angles(0, 84.24478972, offset)
    		loc = bx.calc_angles(100, 84.24478972 + gate_mod, offset)#119.1401242
    	elif leg == 2 :
    		angle = 25
    		loc = bx.calc_angles(0, 98.1783 + gate_mod, offset)
    		#loc = IK().calc_angles(119.1401242, 103.1783, offset)
    	elif leg == 3 :
    		angle = 45
    		loc = bx.calc_angles(0, 84.24478972 + gate_mod, offset)
    		#loc = IK().calc_angles( 119.1401242, 84.24478972, offset)
    	elif leg == 4 :
    		angle = -45
    		loc = bx.calc_angles(0, 84.24478972 + gate_mod, offset)
    		#loc = IK().calc_angles( 119.1401242, 84.24478972, offset)
    	elif leg == 5 :
    		angle = -25
    		loc = bx.calc_angles(0, 98.1783 + gate_mod, offset)#103.1783
    		#loc = IK().calc_angles(119.1401242, 103.1783, offset)
    	elif leg == 6 :
    		angle = -9.73 + angle_modifier
                print "angle mod forward:",angle_modifier
	        print "angle product forward:",angle
    		#loc = IK().calc_angles(0, 84.24478972, offset)
    		loc = bx.calc_angles(100, 84.24478972 + gate_mod, offset)#119.1401242
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
    #@param speed int representing speed between 0 and 1023
    def stapzuruck(self, leg, angle_modifier, gate_mod, speed):
    	#print "zuruck"
    	offset = 71
    	angle = 0
    	loc = [0,0]
    	if leg == 1 :
    		angle = -45
    		loc = bx.calc_angles(0, 84.24478972 + gate_mod, offset)
    		#loc = IK().calc_angles( 119.1401242, 84.24478972, offset)
    	elif leg == 2 :
    		angle = -25
    		loc = bx.calc_angles(0, 103.1783 + gate_mod, offset)
    		#loc = IK().calc_angles(119.1401242, 103.1783, offset)
    	elif leg == 3 :
    		angle = -9.73 + angle_modifier
                print "angle mod backward:",angle_modifier
                print "angle product backward:",angle
    		#loc = IK().calc_angles(0, 84.24478972, offset)
    		loc = bx.calc_angles(100, 84.24478972 + gate_mod, offset)#119.1401242
    	elif leg == 4 :
    		angle = 9.73 + angle_modifier
    		#loc = IK().calc_angles(0, 84.24478972, offset)
    		loc = bx.calc_angles(100, 84.24478972 + gate_mod, offset)#119.1401242
    	elif leg == 5 :
    		angle = 25
    		loc = bx.calc_angles(0, 98.1783 + gate_mod, offset)#103.1783
    		#loc = IK().calc_angles(119.1401242, 103.1783, offset)
    	elif leg == 6 :
    		angle = 45
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
    #@param speed int representing speed between 0 and 1023
    def moveBackward(self, moveAngleLeft, moveAngleRight, gate_mod, left, speed):
        try:
            Movement.isMoving = True
            for x in range(2, 7, 2):
                self.raiselegs(x)
            ax.action()
            #sleep(0.05)
            for x in range(2, 7, 2):
                self.stapzuruck(x, moveAngleRight, gate_mod, speed)
            ax.action()
            #sleep(0.05)
            for x in range(2, 7, 2):
                self.lowerlegs(x)
            ax.action()
            #sleep(0.05)
            for x in range(1, 7, 2):
                self.raiselegs(x)
            ax.action()
            #sleep(0.05)
            for x in range(2, 7, 2):
                self.stapvooruit(x, moveAngleLeft, gate_mod, speed)
            ax.action()
            #sleep(0.05)
            for x in range(1, 7, 2):
                self.stapzuruck(x, moveAngleRight*left, gate_mod, speed)#right
            ax.action()
            #sleep(0.05)
            for x in range(1, 7, 2):
                self.lowerlegs(x)
            ax.action()
            #sleep(0.05)
            for x in range(2, 7, 2):
                self.raiselegs(x)
            ax.action()
            #sleep(0.05)
            for x in range(1, 7, 2):
                self.stapvooruit(x, moveAngleLeft*left, gate_mod, speed)
            ax.action()
            sleep(0.05)

        except:
            try:
                self.rest()
            except:
                pass
        finally:
            Movement.isMoving = False

    ##Moves the hexapod forward using inverse kinematics
    #@param moveAngleLeft Float representing angle modifier used to change walking angle to the left side
    #@param moveAngleRight Float representing angle modifier used to change walking angle to the right side
    #@param gate_mod Float representing distance between body and length in millimeters
    #@param speed int representing speed between 0 and 1023
    def moveForward(self, moveAngleLeft, moveAngleRight, gate_mod, speed):
        try:
            Movement.isMoving = True
            for x in range(2, 7, 2):
                self.raiselegs(x)
            ax.action()
            #sleep(0.05)
            for x in range(2, 7, 2):
                self.stapvooruit(x, moveAngleLeft, gate_mod, speed)#, 8.0
            ax.action()
            #sleep(0.05)
            for x in range(2, 7, 2):
                self.lowerlegs(x)
            ax.action()
            #sleep(0.05)
            for x in range(1, 7, 2):
                self.raiselegs(x)
            ax.action()
            #sleep(0.05)
            for x in range(2, 7, 2):
                self.stapzuruck(x, moveAngleRight, gate_mod, speed)
            ax.action()
            #sleep(0.05)
            for x in range(1, 7, 2):
                self.stapvooruit(x, moveAngleLeft, gate_mod, speed)#, -8.0
            ax.action()
            #sleep(0.05)
            for x in range(1, 7, 2):
                self.lowerlegs(x)
            ax.action()
            #sleep(0.05)
            for x in range(2, 7, 2):
                self.raiselegs(x)
            ax.action()
            #sleep(0.05)
            for x in range(1, 7, 2):
                self.stapzuruck(x, moveAngleRight, gate_mod, speed)
            ax.action()
            sleep(0.05)
        except:
            try:
                self.rest()
            except:
                pass
        finally:
            Movement.isMoving = False

	#turn per 10 degrees
	##moves the hexapod to the right in a certain angle in degrees #hardcoded!
    def turnLeft(self, rotAngle):
        try:
            Movement.isMoving = True
            speed = 300
            #poot omhoog
            ax.moveSpeedRW(12, 750, speed)
            ax.moveSpeedRW(13, 980, speed)
            ax.moveSpeedRW(32, 750, speed)
            ax.moveSpeedRW(33, 980, speed)
            ax.moveSpeedRW(52, 750, speed)
            ax.moveSpeedRW(53, 980, speed)
            ax.action()
            sleep(0.05)

            #draai
            ax.moveSpeedRW(11, int(463 + rotAngle * 0.8), speed)
            ax.moveSpeedRW(31, int(463 + rotAngle * 0.8), speed)
            ax.moveSpeedRW(51, int(478 + rotAngle * 0.8), speed)
            ax.action()
            sleep(0.05)

            #poot omlaag
            ax.moveSpeedRW(12, 656, speed)
            ax.moveSpeedRW(32, 656, speed)
            ax.moveSpeedRW(52, 656, speed)
            ax.action()
            sleep(0.05)

            #poot omhoog
            ax.moveSpeedRW(22, 750, speed)
            ax.moveSpeedRW(23, 980, speed)
            ax.moveSpeedRW(42, 750, speed)
            ax.moveSpeedRW(43, 980, speed)
            ax.moveSpeedRW(62, 750, speed)
            ax.moveSpeedRW(63, 980, speed)
            ax.action()
            sleep(0.05)

            #draai lichaam
            ax.moveSpeedRW(11, 512, speed)
            ax.moveSpeedRW(31, 512, speed)
            ax.moveSpeedRW(51, 512, speed)
            ax.moveSpeedRW(21, int(478+ rotAngle * 0.8), speed)
            ax.moveSpeedRW(41, int(463+ rotAngle * 0.8), speed)
            ax.moveSpeedRW(61, int(463+ rotAngle * 0.8), speed)
            ax.action()
            sleep(0.05)

            #poot omlaag
            ax.moveSpeedRW(22, 656, speed)
            ax.moveSpeedRW(42, 656, speed)
            ax.moveSpeedRW(62, 656, speed)
            ax.action()
            sleep(0.05)

            #poot omhoog
            ax.moveSpeedRW(12, 750, speed)
            ax.moveSpeedRW(13, 980, speed)
            ax.moveSpeedRW(32, 750, speed)
            ax.moveSpeedRW(33, 980, speed)
            ax.moveSpeedRW(52, 750, speed)
            ax.moveSpeedRW(53, 980, speed)
            ax.action()
            sleep(0.05)

            #draai lichaam
            ax.moveSpeedRW(21, 512, speed)
            ax.moveSpeedRW(41, 512, speed)
            ax.moveSpeedRW(61, 512, speed)
            ax.moveSpeedRW(11, int(463+ rotAngle * 0.8), speed)
            ax.moveSpeedRW(31, int(463+ rotAngle * 0.8), speed)
            ax.moveSpeedRW(51, int(478+ rotAngle * 0.8), speed)
            ax.action()
            sleep(0.05)
    	except:
            try:
                self.rest()
            except:
                pass
        finally:
            Movement.isMoving = False



	#turn per 10 degrees
	##moves the hexapod to the right in a certain angle in degrees #hardcoded!
    def turnRight(self, rotAngle):
        try:
            Movement.isMoving = True
            speed = 300
            ax.moveSpeedRW(12, 750, speed)
            ax.moveSpeedRW(13, 980, speed)
            ax.moveSpeedRW(32, 750, speed)
            ax.moveSpeedRW(33, 980, speed)
            ax.moveSpeedRW(52, 750, speed)
            ax.moveSpeedRW(53, 980, speed)
            ax.action()
            sleep(0.05)

            #draai
            ax.moveSpeedRW(11, int(561+ rotAngle * 0.8), speed)
            ax.moveSpeedRW(31, int(561+ rotAngle * 0.8), speed)
            ax.moveSpeedRW(51, int(546+ rotAngle * 0.8), speed)
            ax.action()
            sleep(0.05)

            #poot omlaag
            ax.moveSpeedRW(12, 656, speed)
            ax.moveSpeedRW(32, 656, speed)
            ax.moveSpeedRW(52, 656, speed)
            ax.action()
            sleep(0.05)

            #poot omhoog
            ax.moveSpeedRW(22, 750, speed)
            ax.moveSpeedRW(23, 980, speed)
            ax.moveSpeedRW(42, 750, speed)
            ax.moveSpeedRW(43, 980, speed)
            ax.moveSpeedRW(62, 750, speed)
            ax.moveSpeedRW(63, 980, speed)
            ax.action()
            sleep(0.05)

            #draai lichaam
            ax.moveSpeedRW(11, 512, speed)
            ax.moveSpeedRW(31, 512, speed)
            ax.moveSpeedRW(51, 512, speed)
            ax.moveSpeedRW(21, int(546+ rotAngle * 0.8), speed)
            ax.moveSpeedRW(41, int(561+ rotAngle * 0.8), speed)
            ax.moveSpeedRW(61, int(561+ rotAngle * 0.8), speed)
            ax.action()
            sleep(0.05)

            #poot omlaag
            ax.moveSpeedRW(22, 656, speed)
            ax.moveSpeedRW(42, 656, speed)
            ax.moveSpeedRW(62, 656, speed)
            ax.action()
            sleep(0.05)

            #poot omhoog
            ax.moveSpeedRW(12, 750, speed)
            ax.moveSpeedRW(13, 980, speed)
            ax.moveSpeedRW(32, 750, speed)
            ax.moveSpeedRW(33, 980, speed)
            ax.moveSpeedRW(52, 750, speed)
            ax.moveSpeedRW(53, 980, speed)
            ax.action()
            sleep(0.05)

            #draai lichaam
            ax.moveSpeedRW(21, 512, speed)
            ax.moveSpeedRW(41, 512, speed)
            ax.moveSpeedRW(61, 512, speed)
            ax.moveSpeedRW(11, int(561+ rotAngle * 0.8), speed)
            ax.moveSpeedRW(31, int(561+ rotAngle * 0.8), speed)
            ax.moveSpeedRW(51, int(546+ rotAngle * 0.8), speed)
            ax.action()
            sleep(0.05)
    	except:
            try:
                self.rest()
            except:
                pass
        finally:
            Movement.isMoving = False
    	#for x in range(1, 7):
    	#	self.rest(x)

    def calculateDOF(self,rotationAngle):
        return (60 - 9.73) / 60.0 * rotationAngle

    ##Moves the hexapod forward using joystick-input
    #@param x Float representing x-input from joystick
    #@param y Float representing y-input from joystick
    def movementController(self,x,y):
    	if Movement.isMoving:
    		return
        angle_mod = self.calculateDOF(x)
        angle_mod_inverted = angle_mod *-1
    	if x < 10 and x > -10:
    		if y > 10:
            		print "Move forward"
                	self.moveForward(0,0,0,int(sCalc.speed(x,y)))
    		elif y < -10:
           		print "Move backward"
                	self.moveBackward(0,0,0,1,int(sCalc.speed(x,y)))
                else:
                        self.rest()
    	elif x <= -10 and x >= -50:#move angle to left
            if y >= 0:
                print "Move forward to left"
                self.moveForward(angle_mod, angle_mod_inverted, 0, int(sCalc.speed(x,y)))
            else:
                print "Move backward to left"
                self.moveBackward(angle_mod, angle_mod_inverted, 0, 1, int(sCalc.speed(x,y)))
    	elif x >= 10 and x <= 50:#move angle to right
            if y >= 0:
                print "Move forward to right"
                self.moveForward(angle_mod, angle_mod_inverted, 0, int(sCalc.speed(x,y)))
            else:
                print "Move backward to right"
                self.moveBackward(angle_mod, angle_mod_inverted, 0, -1,int(sCalc.speed(x,y)))
        elif x < -50:
                self.turnLeft(x)
        elif x > 50:
                self.turnRight(x)
        #self.rest()
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

"""try:
	while True:
		Movement().movementController(5.0,30.0)
		#sleep(1)
except KeyboardInterrupt:
	for x in range(1, 7):
    	    Movement().rest(x)
#            ax.action()"""
