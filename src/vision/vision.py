#!/usr/bin/python
import cv2
from multiprocessing import Process, Queue
from recognition import Recognition
from datetime import datetime, timedelta
from camera_pi import Camera


class Vision:
	rec = Recognition()
	lastPosition = None
	lastSize = 0
	lastDirection = None
	buffer = 20
	attackPast = False
	refinedRadius = 600000
	running = False

	def __direction(self, coord, balloon):
		middleX = width / 2
		middleY = height / 2
		if balloon and result[2] >= 900000:
			return "ATTACK"
		if coord[0] >= (middleX - buffer) and coord[0] <= (middleX + buffer):
			return "Forward"
		elif coord[0] <= (middleX - buffer):
			return "Left"
		elif coord[0] >= (middleX + buffer):
			return "Right"

		return None

	def startAutonomousBalloon():
		self.buffer = 80
		self.running = True
		timePrevious = datetime.now()
		timePast = 0
		while(self.running):
			timeNow = datetime.now()
			timePast = (timePrevious - timedelta(timeNow)) / 1000
			timePrevious = timeNow

			if timePast <= 5000 and self.lastDirection == "Forward" and lastSize <= refinedRadius:
				__SpiderAction("Forward")
				continue

			frame =  cam.get_frame()
			coord = __detectLine(frame)

			if coord is not None:
				direction = __direction(coord, True)
				self.lastDirection = direction
				if attackPast and direction is None:# balloon is gone
					rec.resetValues()
					self.running = False
				elif attackPast and coord[2] <= 2000:# balloon is gone, but scraps lying around
					rec.resetValues()
					self.running = False
				elif direction is not None:
					__SpiderAction(direction)
			timePast = 0

		attackPast = False

	def stopAutonomous():
		self.running = False

	def startAutonomousLine():
		self.buffer = 20
		self.running = True
		while(self.running):
			frame =  cam.get_frame()
			coord = __detectLine(frame)

			if coord is not None:
				direction = __direction(coord, False)
				if direction is not None:
					__SpiderAction(direction)
		attackPast = False



	def __SpiderAction(command):
		#command
		pass

	def __detectLine(self, frame):
		self.buffer = 50
		frame = self.__decodeFrame(frame)
		return rec.targetLine(frame)

	def __targetBalloon(self, frame):
		frame = self.__decodeFrame(frame)
		return rec.targetBalloon(frame)

	def __decodeFrame(self, frame):
		data = np.fromstring(frame, dtype=np.uint8)
		return cv2.imdecode(data,1)
