#!/usr/bin/python
import math
##calculates speed based on gyro sensor value between -60 and 60
#@param z Float representing x-value of the gyro-sensor
def omrek(z):			#input: x-waarde
	a = 400.0/60.0
	if z >= 60:
		z=60
	elif z <= -60:
		z=-60
	elif z >= -10 and z <= 10:
		z = 0
	c = a*z
	return math.fabs(c)
	

##calculates angle based on y-value of the gyro sensor
#@param b Float representing y-value of the gyro-sensor
def angleCalc(b):		#input: y-waarde
	startPos = 511.0	
	c=300/1024.0
	angle = startPos + (b*0.75)/c
	print angle
	return angle


##connects the 2 previous methods so they can be used in the main class
#@param a Float representing x-value of the gyro-sensor
#@param b Float representing y-value of the gyro-sensor
def beweging(a,b):
	angleCalc(a)
	omrek(b)

omrek(-60)
	
	
	



