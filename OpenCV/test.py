import cv2
import os
import math
import numpy as np

class Camera:
	def start(self):
		cap = cv2.VideoCapture(0)
		while(1):
			cv2.waitKey(1)
			ref, frame = cap.read()
			hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			lower_red = np.array([0, 50, 100])
			upper_red = np.array([10, 255, 255])
			mask0 = cv2.inRange(hsv, lower_red, upper_red)
			lower_red = np.array([160,50, 100])
			upper_red = np.array([200,255,255])
			mask1 = cv2.inRange(hsv, lower_red, upper_red)

			mask = mask0+mask1
   			#mask = cv2.bitwise_or(mask, frame)

			kernel = np.ones((10,10),np.uint8)
			mask =  cv2.erode(mask,kernel,iterations = 1)

			dilation = np.ones((10, 10), "uint8")
			mask = cv2.dilate(mask, dilation)

			mask = cv2.medianBlur(mask,5)

			circles = cv2.HoughCircles(mask,cv2.HOUGH_GRADIENT,1.4,50,param1=80,param2=70,minRadius=1, maxRadius=36000)
			if circles is None:
				cv2.imshow('mask',mask)
				#cv2.imshow('raw',frame)
				#cv2.waitKey(1) #system sleep anders verdwijnt screen
				continue

			#circles = np.uint16(np.around(circles))
			for i in circles[0,:]:
				cv2.circle(mask,(i[0],i[1]),2,(0,0,255),3)
				cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)


			cv2.imshow('mask',mask)
			cv2.imshow('frame',frame)

			k = cv2.waitKey(5) & 0xFF
			if k == 27:
				cap.release()
				break
		cv2.destroyAllWindows()
