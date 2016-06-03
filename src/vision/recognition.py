import cv2
import math
import numpy as np
from morphology import Morphology

class Recognition:
	morph = Morphology()
	lastPosition = None
	framesRequired = 3
	count = 0

	cropHeight = 30
	bufferX = 10
	bufferY = 100
	##Resets all internal values used within the Recognition class
	def resetValues(self):
		self.count = 0
		self.lastPosition = None

	##Edits frame into a smaller section, thresholds and detects a white line.
	#@param frame decoded frame.
	#returns array containing X and Y of line, returns none if no line was found.
	def targetLine(self, frame):
		if frame is None:
			 return None
		frame = self.__cropFrame(frame)

		lower_white = np.array([0, 0, 190])
		upper_white = np.array([180, 255, 255])
		thresholded = self.morph.thresholdImage(frame, lower_white, upper_white)

		mask = self.morph.morphFrame(thresholded)

		#mask = cv2.GaussianBlur(mask,(5,5),0)
		#mask = self.morph.floodFill(mask)		

		return self.__detectLine(mask)

	##Thresholds frame on red and edits the frame to remove noise and detects the largest red blob.
	#@param frame decoded frame.
	#returns array containing X, Y and Area of detected blob, returns none if no blob was detected
	def targetBalloon(self, frame):
		if frame is None:
			 return None

		lower_red = np.array([0, 100, 60])
		upper_red = np.array([10, 255, 255])
		thresholded = self.morph.thresholdImage(frame, lower_red, upper_red)

		mask = self.morph.morphFrame(thresholded)

		mask = self.morph.floodFill(mask)

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
	'''
	#houghCircle can only detect circles at 3 meters max, unless resolution is increased. 
	#However greater resolution can solve this, but this increases computation time
	# def __detectCircleHough(self,frame):
	# 	radius = 0
	# 	circles = cv2.HoughCircles(frame,cv.CV_HOUGH_GRADIENT,2.5,50,param1=80,param2=70,minRadius=0, maxRadius=3000)
	#
	# 	if circles is None:
	# 		return None
	#
	# 	position = None
	# 	for i in circles[0,:]:
	# 		if radius < i[2]:
	# 			position = i
	# 	return position'''

	##detects blob with the greatest area and returns X,Y and area of this blob
	#@param mask binary mask where detection is performed
	#Returns X, Y coordinates and area of this blob, returns None if no blob was detected
	def __detectCircleBlob(self,mask):
		#contours = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]
		image, contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)		
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
	
	##Detects line with a rectangle and returns coordinates
	#@param croppedImage Binary image used to find line, use smaller resolution for efficienty
	#Returns the upperleft X and Y Coordinates of the line
	def __detectLine(self,croppedImage):
		#contours = cv2.findContours(croppedImage,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]
		im2, contours, hierarchy = cv2.findContours(croppedImage,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		#image, contours, hierarchy = cv2.findContours(croppedImage,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		if len(contours) == 0:
			return None
	    	max_area = 0
		best_cnt = None
		x = 0
		y = 0
		for cnt in contours:
			area = cv2.contourArea(cnt)
			M = cv2.moments(cnt)
			if M["m00"] != 0:
				if area > max_area:
					max_area = area
            				best_cnt = cnt
					x,y,w,h = cv2.boundingRect(cnt)
		return [x + self.bufferX, y + self.bufferY]


	##crops frame in much smaller resolution and returns the newly created frame
	#@param frame full sized frame that needs to be cropped
	#returns a portion of the supplied frame
	def __cropFrame(self, frame):
		rows, cols = frame.shape[:2]
		x2 = cols - self.bufferX
		x1 = self.bufferX
		y1 = rows - self.bufferY
		y2 = y1 + self.cropHeight

		return frame[y1: y2, x1:x2]

