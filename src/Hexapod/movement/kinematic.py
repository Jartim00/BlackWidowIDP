#!/usr/bin/python
import math
import os

class kinematic:

	tibia = 124
	femur = 78
	coxa = 37
	offset = 71
	servo_beta = 0
	servo_alpha = 0
	_FACTOR = 300.0/1024.0 #omrekenfactor van graden naar stappen
	
	#   |\
	#	|  \
	#	|	 \
	#	|	   \
	#	|		 \
	#	|		   \
	# x	|			 \	
	#	|			   \
	#	|				 \
	#	|                  \
	#	|                    \
	#	|______________________\ < -- Position of Servo
	#			y
	#Input x,y,z
	# x = length of a step
	# y = length of the leg
	# z = height between body and floor
	# Formula source: http://kkulhanek.blogspot.nl/2013/01/inverse-kinematics-for-3-dof-hexapod.html
	
	##Calculates Alpha and Beta to an angle a servo can read, will print all the steps necessary for debug purposes.
	#@param x length of a step
	#@param y length of the leg
	#@param z height between body and floor
	def calc_angles_debug(self,x,y,z):
		L1 = math.sqrt(x**2+ y**2)
		print "L1: ",L1
		gama = math.atan(x/y)/math.pi * 180
		print "Gama: ",gama
		L = math.sqrt(((L1 - self.coxa)**2)+z**2)
		print "L: ", L
		beta = math.acos((self.tibia**2 + self.femur**2 - L ** 2)/ (2*self.tibia*self.femur)) / math.pi * 180
		print "beta: ",beta
		alpha1 = math.acos(z/L)/math.pi*180
		print "alpha1: ",alpha1
		alpha2 = math.acos((self.femur**2+ L**2 - self.tibia**2)/(2*self.femur*L)) / math.pi * 180
		print "alpha2: ",alpha2
		alpha = alpha1 + alpha2
		print "alpha: ",alpha
		self.servo_beta = int(512 + ((180 - beta) / self._FACTOR))
		print "beta in servo angle: ", int(512 + ((180 - beta) / self._FACTOR))
		self.servo_alpha = int(512 + ((alpha2 - (math.atan(self.offset / (L1 - self.coxa)) / math.pi * 180)) / self.FACTOR))
		print "alpha in servo angle: ", int(512 + ((alpha2 - (math.atan(self.offset / (L1 - self.coxa)) / math.pi * 180)) / self._FACTOR))

	##Calculates Alpha and Beta to an angle a servo can read.
	#@param x length of a step
	#@param y length of the leg
	#@param z height between body and floor	
	def calc_angles(self,x,y,z):
		L1 = math.sqrt(x ** 2 + y ** 2)
		L = math.sqrt(((L1 - self.coxa) ** 2) + z ** 2)
		beta = math.acos((self.tibia ** 2 + self.femur ** 2 - L ** 2) / (2 * self.tibia * self.femur)) / math.pi * 180
		alpha2 = math.acos((self.femur ** 2 + L ** 2 - self.tibia ** 2) / (2 * self.femur * L)) / math.pi * 180
		self.servo_alpha = int(512 + ((alpha2 - (math.atan(self.offset / (L1 - self.coxa)) / math.pi * 180)) / self._FACTOR))
		if self.servo_alpha > 1023: self.servo_alpha = 1023
		self.servo_beta = int(512 + ((180 - beta) / self._FACTOR))
		if self.servo_beta > 1023: self.servo_beta = 1023

		return [self.servo_alpha,self.servo_beta]

	##Convert an angle to a position the servo can read.
	#@param x angle in degrees		
	def AngleToServo(x):
		return int(512 + (x / self._FACTOR))	

	def __init__(self):
		pass
