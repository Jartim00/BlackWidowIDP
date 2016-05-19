import cv2
import os
import math

from multiprocessing import Queue

#http://elinux.org/Rpi_Camera_Module
class Recognition:
	#lastPosition = None
	framesRequired = 5
	count = 0
	lastPosition = None
	radius = 0
	def targetBalloon(self,q, frameQue):
		while(True):
			if frameQue.empty():
				print "frameQue out"
				continue

			frame = frameQue.get()
			frame = cv2.flip(frame, 1)
			frame = cv2.medianBlur(frame,5)
			hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			lower_red = np.array([0, 100, 60])
			upper_red = np.array([10, 255, 255])
			mask0 = cv2.inRange(hsv, lower_red, upper_red)
			lower_red = np.array([170,100, 60])
			upper_red = np.array([200,255,255])
			mask1 = cv2.inRange(hsv, lower_red, upper_red)

			#mask = cv2.multiply(mask0,mask1)
			#mask = mask0+mask1
			mask = mask1

			kernel = np.ones((20, 20), "uint8")
			opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

			kernel = np.ones((8, 8), "uint8")
			mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
		
			kernel = np.ones((20, 20), "uint8")
			opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
		
			kernel = np.ones((8,8),np.uint8)			
			mask =  cv2.erode(mask,kernel,iterations = 1)

			kernel = np.ones((12, 12),np.uint8)
			mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

			kernel = np.ones((20, 20), "uint8")
			mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
		
			im_floodfill = mask.copy()			 
			h, w = mask.shape[:2]
			kernel = np.zeros((h+2, w+2), np.uint8)
			cv2.floodFill(im_floodfill, kernel, (0,0), 255);
		
			im_floodfill_inv = cv2.bitwise_not(im_floodfill)
		
			#mask = mask | im_floodfill_inv
			mask = mask | im_floodfill_inv
			mask = cv2.medianBlur(mask,5)
		
			circles = cv2.HoughCircles(mask,cv2.HOUGH_GRADIENT,2.2,50,param1=80,param2=70,minRadius=0, maxRadius=36000)
		
			if circles is None:
				cv2.imshow('mask',mask)
				cv2.imshow('frame',frame)
				self.count = 0
				return None

			#circles = np.uint16(np.around(circles))
			lc = None
			for i in circles[0,:]:
				if radius < i[2]:
					lc = i
			radius = 0

			if lastPosition is None:
				lastPosition = lc
			elif withinBounds(lastPosition,lc):
				lastPosition = lc
				print "within bounds"
			else:
				lastPosition = None
				radius = 0
				distance = 2 * math.pi * lc[2]

		        self.count += 1
		
			if self.count >= self.framesRequired:
				q.put(lastPosition)
				print "LOCK ON"
			print self.count

def withinBounds(previous, position):
	spread = 80
	if (position[0] - spread) >= previous[0] and (position[0] + spread) <= previous[0] and (position[1] - spread) >= previous[1] and (position[1] + spread) <= previous[1]:
		return True
	return False
		
	
