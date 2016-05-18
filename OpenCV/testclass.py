#!/usr/bin/python
import time
import numpy as np
from multiprocessing import Process, Queue

from camera_pi import Camera
from recognition import Recognition

lastPosition = None
width = 640
height = 480
buffer = 20
def direction(coord):
	middleX = width / 2
	middleY = height / 2
	if coord[0] >= (middleX - buffer) and coord[0] <= (middleX + buffer):
		return "Forward"
	elif coord[0] <= (middleX - buffer):
		return "Left"
	elif coord[0] >= (middleX + buffer):
		return "Right"

	return "False"


if __name__ == '__main__':
	Camera().initialize()	
	frameQue = Queue()
	que = Queue()
	p = Process(target=Recognition().targetBalloon, args=(que,frameQue,))
	p.start()	
	while(True):
		frame = camera.get_frame()
		frame = np.fromstring(frame, dtype=np.uint8)
		frameQueue.put(frame)
		if not que.empty():
			lastPosition = que.get_nowait()
			temp = direction(lastPosition)			
			print temp
	p.join()
