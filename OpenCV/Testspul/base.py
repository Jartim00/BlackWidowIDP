#!/usr/bin/python
from multiprocessing import Process, Queue
from recognition import Recognition
import cv2

cam = Camera()
rec = Recognition()

lastPosition = None
width = 640
height = 480
buffer = 20
def direction(coord):
	middleX = width / 2
	middleY = height / 2
	if coord[0] >= (middleX - buffer) and coord[0] <= (middleX + buffer):
		return "Forward"
	elif coord[0] <= (middleX - buffer):
		return "Left"
	elif coord[0] >= (middleX + buffer):
		return "Right"

	return "False"
if __name__ == '__main__':

	while(True):
		frame =  cam.get_frame()
		result = rec.targetBalloon(frame)
		#lastPosition = que.get()

		if result is not None:
			temp = direction(result)
			rangeObject = result[2] / 5.32
			print temp
			print "cm: " + rangeObject
		#elif:
			
