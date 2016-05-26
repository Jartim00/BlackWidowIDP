import cv2
import cv2.cv as cv
import os
import PIL
import math
import numpy as np
from multiprocessing import Queue

#http://elinux.org/Rpi_Camera_Module
class Recognition:
	lastPosition = None
	framesRequired = 3
	count = 0

	def targetBalloon(self, frame):
		if frame is None:
			 return None
		#e1 = cv2.getTickCount()
		data = np.fromstring(frame, dtype=np.uint8)
		frame = cv2.imdecode (data,1)
		#cv2.imshow('clean', frame)
		#cv2.waitKey(1)
		#e2 = cv2.getTickCount()
		#time = (e2 - e1)/ cv2.getTickFrequency()		
		#print "Decode time: "+  str(time)

		#e1 = cv2.getTickCount()
		mask = self.thresholdImage(frame)
		#e2 = cv2.getTickCount()
		#time = (e2 - e1)/ cv2.getTickFrequency()		
		#print "Threshold time: "+  str(time)

		#e1 = cv2.getTickCount()
		mask = self.morphFrame(mask)
		#e2 = cv2.getTickCount()
		#time = (e2 - e1)/ cv2.getTickFrequency()		
		#print "Morph time: "+  str(time)

		#e1 = cv2.getTickCount()		
		mask = self.floodFill(mask)		
		#e2 = cv2.getTickCount()
		#time = (e2 - e1)/ cv2.getTickFrequency()		
		#print "floodfill time: "+  str(time)

		mask = cv2.medianBlur(mask,5)
		#cv2.imshow('frame', mask)
		#cv2.waitKey(1)
		currentCoordinate = self.detectCircle(mask)
			
		if currentCoordinate is None:
			self.count = 0
			return None
		if self.lastPosition is None:
			self.lastPosition = currentCoordinate
		elif self.withinBounds(self.lastPosition,currentCoordinate):
			self.lastPosition = currentCoordinate
			print "within bounds"
		else:
			self.lastPosition = None

                self.count += 1
		#print str(self.count)

		if self.count >= self.framesRequired:
			#print "LOCK ON"			
			return self.lastPosition
	
		return None

	def thresholdImage(self,frame):
		#frame = cv2.medianBlur(frame,5)
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		lower_red = np.array([0, 50, 60])#[0, 50, 100]
		upper_red = np.array([10, 255, 255])
		mask0 = cv2.inRange(hsv, lower_red, upper_red)
			
		#lower_red = np.array([165,100, 40])#[170,50, 100]
		#upper_red = np.array([200,255,255])#200
		#mask1 = cv2.inRange(hsv, lower_red, upper_red)
		return mask0	

	def morphFrame(self,frame):
		kernel = np.ones((20, 20), "uint8")
		opening = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)

		kernel = np.ones((8, 8), "uint8")
		frame = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel)
	
		#kernel = np.ones((20, 20), "uint8")
		#opening = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)
	
		#kernel = np.ones((8,8),np.uint8)			
		#frame =  cv2.erode(frame,kernel,iterations = 1)

		#kernel = np.ones((12, 12),np.uint8)
		#frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)

		#kernel = np.ones((20, 20), "uint8")
		#frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)	
		return frame

	def floodFill(self,frame):
		im_floodfill = frame.copy()			 
		h, w = frame.shape[:2]
		kernel = np.zeros((h+2, w+2), np.uint8)
		cv2.floodFill(im_floodfill, kernel, (0,0), 255)
		im_floodfill_inv = cv2.bitwise_not(im_floodfill)
		frame = frame | im_floodfill_inv
		return frame

	'''def detectCircle(self,frame):
		radius = 0
		circles = cv2.HoughCircles(frame,cv.CV_HOUGH_GRADIENT,2.5,50,param1=80,param2=70,minRadius=0, maxRadius=3000)
	
		if circles is None:
			return None

		position = None
		for i in circles[0,:]:
			if radius < i[2]:
				position = i
		return position'''
	
	def detectCircle(self,mask):
		#image, contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		contours = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]
		#print len(contours)

		height, width = mask.shape[:2]
		middleThree = height / 3
		#cv2.imshow('mask', mask)
	    	max_area = 0
		best_cnt = None
		if len(contours) == 0:
			return None

    		for cnt in contours:
        		area = cv2.contourArea(cnt)
			M = cv2.moments(cnt)
			if M["m00"] != 0:
				cy = int(M['m01']/M['m00'])
				if area > max_area and cy >= middleThree:
					max_area = area
            				best_cnt = cnt
		if best_cnt is None:
			return None
	    	M = cv2.moments(best_cnt)
		cx, cy = 0, 0
		if M["m00"] != 0:
		    cx = int(M["m10"] / M["m00"])
		    cy = int(M["m01"] / M["m00"])
		else:
    			cx, cy = 0, 0
		return [cx, cy, max_area]


	def withinBounds(self, previous, position):
		spread = 80
		if (position[0] - spread) >= previous[0] and (position[0] + spread) <= previous[0] and (position[1] - spread) >= previous[1] and (position[1] + spread) <= previous[1]:
			return True
		return False
		
	
