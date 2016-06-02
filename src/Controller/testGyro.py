#!/usr/bin/python
import random
import spidercommunication
from time import sleep

bt_spider = spidercommunication.SpiderCommunication("00:1A:7D:DA:71:06",1)
def testGyro():
	try:
		bt_spider.start()
		while True:
			randomx = random.randint(-36,35)
			gyropos = [randomx,1,2]
			bt_spider.setGyro(gyropos)
			sleep(0.5)
	except KeyboardInterrupt:
		return -1
	return 0
if __name__ == "__main__":
	testGyro()
