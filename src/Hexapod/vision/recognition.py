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
	bufferX = 50
	bufferY = 100

	def resetValues(self):
		self.count = 0
		self.lastPosition = None

	#return array containing X and Y of line
	def targetLine(self, frame):
		if frame is None:
			 return None
		frame = self.__cropFrame(frame)
		lower_white = np.array([0, 0, 130])
		upper_white = np.array([40, 56, 255])
		thresholded = self.morph.thresholdImage(frame, lower_white, upper_white)
		mask = self.morph.morphFrame(thresholded)
		mask = cv2.bitwise_not(mask)
		#mask = cv2.GaussianBlur(mask,(5,5),0)
		#mask = self.morph.floodFill(mask)
		return self.__detectLineBlob(mask)

	def targetLineDebug(self, frame):
		data = np.fromstring(frame, dtype=np.uint8)
		frame = cv2.imdecode(data,1)
		if frame is None:
			 return None
		frame = self.__cropFrame(frame)
		lower_white = np.array([0, 0, 130])
		upper_white = np.array([40, 56, 255])
		thresholded = self.morph.thresholdImage(frame, lower_white, upper_white)
		mask = self.morph.morphFrame(thresholded)
		#r, bufferIMG = cv2.imencode('.jpeg', mask)
		return mask

	#returns array containing X, Y and Area
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
	# 	return position

	#detects blob with the greatest area and returns X,Y and area of this blob
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

	#crops frame in much smaller resolution and returns the newly created frame
	def __cropFrame(self, frame):
		rows, cols = frame.shape[:2]
		x2 = cols
		x1 = 0
		y1 = rows - Recognition.bufferX
		y2 = rows
		return frame[y1: y2, x1:x2]

	def __detectLine(self,croppedImage):
		#contours = cv2.findContours(croppedImage,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]
		im2, contours, hierarchy = cv2.findContours(croppedImage,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		#image, contours, hierarchy = cv2.findContours(croppedImage,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		if len(contours) == 0:
			return None
	    	max_area = 0
		best_cnt = None
		for cnt in contours:
			area = cv2.contourArea(cnt)
			M = cv2.moments(cnt)
			if M["m00"] != 0:
				if area > max_area:
					max_area = area
            				best_cnt = cnt
					x,y,w,h = cv2.boundingRect(cnt)
		return [x + self.bufferX, y + self.bufferY]

	def __detectLineBlob(self,croppedImage):
		image, contours, hierarchy = cv2.findContours(croppedImage,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

		max_area = 0
		best_cnt = None
		if len(contours) == 0:
			return None

		for cnt in contours:
			area = cv2.contourArea(cnt)
			M = cv2.moments(cnt)
			if M["m00"] != 0:
				if area > max_area:
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
		return [cx, cy]
