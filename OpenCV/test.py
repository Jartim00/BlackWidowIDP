import cv2
import os
import math
import numpy as np

class Camera:
	lastPosition = None
	framesRequired = 10
	count = 0
	def start(self):
		cap = cv2.VideoCapture(0)
		while(1):
			cv2.waitKey(1)
			ref, frame = cap.read()
			hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			lower_red = np.array([0, 50, 100])
			upper_red = np.array([6, 255, 255])
			mask0 = cv2.inRange(hsv, lower_red, upper_red)
			lower_red = np.array([170,50, 100])
			upper_red = np.array([200,255,255])
			mask1 = cv2.inRange(hsv, lower_red, upper_red)

			mask = mask0+mask1

			kernel = np.ones((10,10),np.uint8)
			mask =  cv2.erode(mask,kernel,iterations = 1)

			dilation = np.ones((8, 8), "uint8")
			mask = cv2.dilate(mask, dilation)

			mask = cv2.medianBlur(mask,5)

			circles = cv2.HoughCircles(mask,cv2.HOUGH_GRADIENT,1.9,50,param1=80,param2=70,minRadius=1, maxRadius=3600)
			if circles is None:
				cv2.imshow('mask',mask)
				count = 0
				continue

			#circles = np.uint16(np.around(circles))
			for i in circles[0,:]:
				lastPosition = i
				cv2.circle(mask,(i[0],i[1]),2,(0,0,255),3)
				cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)


			cv2.imshow('maskShot',mask)
			cv2.imshow('frameShot',frame)
                        count += 1
			
			print "X: "+ str(lastPosition[0]) + " Y: " + str(lastPosition[1]) + " radius: " + str(lastPosition[2])

			k = cv2.waitKey(5) & 0xFF
			if k == 27:
				cap.release()
				break
		cv2.destroyAllWindows()
