#!/usr/bin/python
import cv2
import numpy as np
from movement.vooruit import vooruit as movement
from multiprocessing import Process, Queue
from recognition import Recognition
from datetime import datetime, timedelta
from camera_pi import Camera
from recognition import Recognition


class Vision:
	rec = Recognition()
	cam = Camera()
	lastPosition = None
	lastSize = 0
	lastDirection = None
	buffer = 20
	attackPast = False
	refinedRadius = 600000
	running = False
	width = 640
	height = 480
	
	##Returns command to be taken in string format
	#@param coord An array containing [X, Y] or an array containing [X,Y,Area]
	#@param balloon boolean that represents the different actions to take 
	def __direction(self, coord, balloon):
		middleX = self.width / 2
		if balloon and coord[2] >= 900000:
			return "Attack"
		if coord[0] >= (middleX - self.buffer) and coord[0] <= (middleX + self.buffer):
			return "Forward"
		elif coord[0] <= (middleX - self.buffer):
			return "Left"
		elif coord[0] >= (middleX + self.buffer):
			return "Right"

		return None
	
	##starts autonomousLine sequence, which controls the spider. it needs to run on different thread!
	def startAutonomousLine(self):
		self.buffer = 50
		self.running = True
		while(self.running):
			frame =  self.cam.get_frame()
			coord = self.__detectLine(frame)

			if coord is not None:
				direction = self.__direction(coord, False)
				if direction is not None:
					self.__SpiderAction(direction)
		attackPast = False

	##starts autonomous balloon detection sequence, which controls the spider. it needs to run on different thread!
	def startAutonomousBalloon(self):
		self.buffer = 80
		self.running = True
		timePrevious = datetime.now()
		timePast = 0
		while(self.running):
			'''
			timeNow = datetime.now()
			#timePast = (timePrevious - timedelta(timeNow)) / 1000
			#timePrevious = timeNow
			#if self.lastSize <= self.refinedRadius:
			#if timePast <= 5000 and self.lastDirection == "Forward" and lastSize <= refinedRadius:
			#	__SpiderAction("Forward")
			#	continue'''

			frame =  self.cam.get_frame()
			coord = self.__targetBalloon(frame)

			if coord is not None:
				direction = self.__direction(coord, True)
				print coord
				self.lastDirection = direction
				self.lastSize = coord[2]
				if self.attackPast and direction is None:# balloon is gone
					self.rec.resetValues()
					self.running = False
				elif self.attackPast and coord[2] <= 2000:# balloon is gone, but scraps lying around
					self.rec.resetValues()
					self.running = False
				elif direction is not None:
					self.__SpiderAction(direction)
			timePast = 0

		self.attackPast = False

	##used to stop the infinite loop of autonomy mode
	def stopAutonomous(self):
		self.running = False

	##Translates string action to a predefined Movement pattern
	#@param command string command of which action the spider has to take
	def __SpiderAction(self,command):
		print command
		if command == "Forward":
			movement().vooruit()
		elif command == "Left":
			movement().links()
		elif command == "Right":
			movement().rechts()
		elif command == "Attack":
			pass
		movement().rust()
	
	##decodes frame and returns x y coordinates of line
	#@param frame raw jpeg image captured from a camera
	#Returns X and Y coordinate of line in array form [X,Y]
	def __detectLine(self, frame):
		frame = self.__decodeFrame(frame)
		return self.rec.targetLine(frame)
	
	#decodes frame and returns x y coordinates and area of balloon 
	#@param frame raw jpeg image captured from a camera
	#Returns X and Y coordinate and the area of balloon in array form [X,Y, Area]
	def __targetBalloon(self, frame):
		frame = self.__decodeFrame(frame)
		return self.rec.targetBalloon(frame)

	##decodes frame from string to a Numphy array
	#@param frame raw jpeg image captured from a camera
	#Returns image in numphpy array format
	def __decodeFrame(self, frame):
		data = np.fromstring(frame, dtype=np.uint8)
		return cv2.imdecode(data,1)
