#!/usr/bin/python
import math

class Speedcalculation:
	##calculates speed based on gyro sensor's x-and-y-value between -60 and 60
	#@param x Float representing x-value of the gyro-sensor
	#@param y Float representing y-value of the gyro-sensor		
	maxSpeed = 511
	unit = maxSpeed/60.0
	def speed(self,x,y):			#input: x-waarde
		r = math.sqrt(x ** 2 + y ** 2)*self.unit
		if r <= self.maxSpeed and r >= 120:
			print r
		elif r >= 120:
			print self.maxSpeed
		else:
			print 0

	##calculates angle based on y-value of the gyro sensor
	#@param b Float representing y-value of the gyro-sensor
	def angleCalc(self,b):		#input: y-waarde
		startPos = 511.0	
		c=300/1024.0
		angle = startPos + (b*0.75)/c
		print angle
		return angle



