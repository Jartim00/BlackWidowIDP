#!/usr/bin/python
import cv2
import numpy as np

class Morphology:
	
	#frame is decoded image
	#lower is the lower range of threshold, type in np.array
	#upper is the upper range of threshold, type is np.array
	def thresholdImage(self,frame, lower, upper):
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		return cv2.inRange(hsv, lower, upper)

	#cleans noise from image
	def morphFrame(self,frame):
		kernel = np.ones((20, 20), "uint8")
		opening = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)

		kernel = np.ones((8, 8), "uint8")
		frame = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel)	
		return frame

	#fills holes in established blobs
	def floodFill(self,frame):
		im_floodfill = frame.copy()			 
		h, w = frame.shape[:2]
		kernel = np.zeros((h+2, w+2), np.uint8)
		cv2.floodFill(im_floodfill, kernel, (0,0), 255)
		im_floodfill_inv = cv2.bitwise_not(im_floodfill)
		frame = frame | im_floodfill_inv
		return frame
