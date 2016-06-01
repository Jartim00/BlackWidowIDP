#!/usr/bin/python
import cv2
import numpy as np
from movement.vooruit import vooruit as movement
from multiprocessing import Process, Queue
from recognition import Recognition
from datetime import datetime, timedelta
from camera_pi import Camera
from recognition import Recognition


class vision:
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

	def __direction(self, coord, balloon):
		middleX = self.width / 2
		if balloon and coord[2] >= 900000:
			return "ATTACK"
		if coord[0] >= (middleX - self.buffer) and coord[0] <= (middleX + self.buffer):
			return "Forward"
		elif coord[0] <= (middleX - self.buffer):
			return "Left"
		elif coord[0] >= (middleX + self.buffer):
			return "Right"

		return None


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


	def startAutonomousBalloon(self):
		self.buffer = 80
		self.running = True
		timePrevious = datetime.now()
		timePast = 0
		while(self.running):
			timeNow = datetime.now()
			#timePast = (timePrevious - timedelta(timeNow)) / 1000
			#timePrevious = timeNow
			#if self.lastSize <= self.refinedRadius:
			#if timePast <= 5000 and self.lastDirection == "Forward" and lastSize <= refinedRadius:
			#	__SpiderAction("Forward")
			#	continue

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

	def stopAutonomous(self):
		self.running = False

	def __SpiderAction(self,command):
		print command
		if command == "Forward":
			movement().vooruit()
		elif command == "Left":
			movement().links()
		elif command == "Right":
			movement().rechts()
		movement().rust()

	def __detectLine(self, frame):
		frame = self.__decodeFrame(frame)
		return self.rec.targetLine(frame)

	def __targetBalloon(self, frame):
		frame = self.__decodeFrame(frame)
		return self.rec.targetBalloon(frame)

	def __decodeFrame(self, frame):
		data = np.fromstring(frame, dtype=np.uint8)
		return cv2.imdecode(data,1)
