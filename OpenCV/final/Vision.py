#!/usr/bin/python
from multiprocessing import Process, Queue
from recognition import Recognition
from camera import Camera
import cv2


class Vision:
	print "class"
	cam = Camera()
	rec = Recognition()

	lastPosition = None
	buffer = 20

	def __direction(self, coord):
		middleX = width / 2
		middleY = height / 2
		if coord[0] >= (middleX - buffer) and coord[0] <= (middleX + buffer):
			return "Forward"
		elif coord[0] <= (middleX - buffer):
			return "Left"
		elif coord[0] >= (middleX + buffer):
			return "Right"

		return None

	def detectLine(self, frame)
		self.buffer = 20
		frame = self.__decodeFrame(frame)
		return __direction(rec.targetLine(frame))

	def targetBalloon(self, frame)
		self.buffer = 80
		frame = self.__decodeFrame(frame)
		return __direction(rec.targetBalloon(frame))

	def __decodeFrame(self, frame)
		data = np.fromstring(frame, dtype=np.uint8)
		return cv2.__imdecode(data,1)
		
