#!/usr/bin/python
def omrek(z):			#input: x-waarde
	a = 400.0/60.0
	if z >= 60:
		z=60
	elif z <= -60:
		z=-60
	elif z >= -10 and z <= 10:
		z = 0
	omrek = a*z
	print omrek
	return omrek

def angleCalc(b):		#input: y-waarde
	startPos = 511.0	
	c=300/1024.0
	angle = startPos + (b*0.75)/c
	print angle
	return angle

def beweging(a,b):
	omrek(a)
	angleCalc(b)
	
	
beweging(60,60)


