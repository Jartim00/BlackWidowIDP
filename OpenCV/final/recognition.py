import cv2
import cv2.cv as cv
import math
import numpy as np
from morphology as Morphology

class Recognition:
	morph = Morphology()

	lastPosition = None
	framesRequired = 3
	count = 0

	cropHeight = 30
	bufferX = 10
	bufferY = 100

	def resetValues(self):
		count = 0
		lastPosition = None

	#return array containing X and Y
	def targetLine(self, frame):
		if frame is None:
			 return None
		frame = self.__cropFrame(frame)

		lower_white = np.array([0, 0, 190])
		upper_white = np.array([180, 255, 255])
		mask = morph.thresholdImage(frame, lower_white, upper_white)

		#add morph action here if unsatisfied with mask, as is now the test results work

		mask = morph.floodFill(mask)		
		mask = cv2.GaussianBlur(mask,(5,5),0)

		return self.__detectLine(mask)

	#returns array containing X, Y and Area	
	def targetBalloon(self, frame):
		if frame is None:
			 return None

		lower_red = np.array([0, 100, 60])
		upper_red = np.array([10, 255, 255])
		mask = morph.thresholdImage(mask, lower_red, upper_red)
		
		mask = morph.morphFrame(frame)

		mask = morph.floodFill(mask)		

		mask = cv2.medianBlur(mask,5)

		currentCoordinate = self.__detectCircleBlob(mask)
			
		if currentCoordinate is None:
			self.count = 0
			self.lastPosition = None
			return None
		
		self.lastPosition = currentCoordinate
		
                self.count += 1

		if self.count >= self.framesRequired:			
			return self.lastPosition
	
		return None

	def __detectCircleHough(self,frame):
		radius = 0
		circles = cv2.HoughCircles(frame,cv.CV_HOUGH_GRADIENT,2.5,50,param1=80,param2=70,minRadius=0, maxRadius=3000)
	
		if circles is None:
			return None

		position = None
		for i in circles[0,:]:
			if radius < i[2]:
				position = i
		return position
	
	def __detectCircleBlob(self,mask):
		contours = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]
		height, width = mask.shape[:2]
		middleThree = height / 3

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

	def __cropFrame(self, frame):
		rows, cols = frame.shape[:2]
		x2 = cols - self.bufferX
		x1 = self.bufferX
		y1 = rows - self.bufferY
		y2 = y1 + self.cropHeight

		return frame[y1: y2, x1:x2]

	def __detectLine(self,croppedImage):
		image, contours, hierarchy = cv2.findContours(croppedImage,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		if len(contours) == 0:
			return None
		for cnt in contours:
			M = cv2.moments(cnt)
			if M["m00"] != 0:	
				x,y,w,h = cv2.boundingRect(cnt)
		return [x + self.bufferX, y + self.bufferY]
