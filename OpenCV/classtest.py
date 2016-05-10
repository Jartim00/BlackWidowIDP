#!/usr/bin/python
from multiprocessing import Process, Queue

from test import Camera
cam = Camera()
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
	que = Queue()
	p = Process(target=cam.targetLock, args=(que,))
	p.start()
	while(True):
		if not que.empty():
			lastPosition = que.get_nowait()
			temp = direction(lastPosition)
						
			print temp
		#elif:
			
