#!/usr/bin/python
import numpy as np
from multiprocessing import Process, Queue
from recognition import Recognition
from camera_pi import Camera

cam = Camera()
rec = Recognition()

lastPosition = None
width = 640
height = 480
buffer = 100

def direction(coord):
	middleX = width / 2
	middleY = height / 2
	if result[2] >= 900000:
		return "ATTACK"
	elif coord[0] >= (middleX - buffer) and coord[0] <= (middleX + buffer):
		return "Forward"
	elif coord[0] <= (middleX - buffer):
		return "Left"
	elif coord[0] >= (middleX + buffer):	
		return "Right"
	return "False"

if __name__ == '__main__':

	while(True):
		frame =  cam.get_frame()
		print "getting frame" 
		result = rec.targetBalloon(frame)
		print "frame calculated"
		if result is not None:
			temp = direction(result)
			rangeObject = result[2]
			print temp
			print "Area: " + str(rangeObject)
		#elif:
			
