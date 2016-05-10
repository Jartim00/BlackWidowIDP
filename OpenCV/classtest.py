#!/usr/bin/python
from multiprocessing import Process, Queue

from test import Camera
cam = Camera()

if __name__ == '__main__':
	que = Queue()
	p = Process(target=cam.targetLock, args=(que,))
	p.start()
	while(True):
		if not que.empty():
			print str(que.get_nowait())
