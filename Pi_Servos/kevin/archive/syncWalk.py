#!/usr/bin/python
from ax import Ax12
from time import sleep

ax = Ax12()
_DELAY = 0.9
_SPEED = 513

def move():
#	ax.moveSpeedRW(21,700,650)
#	ax.moveSpeedRW(31,300,650)
	ax.moveSpeedRW(22,300,650)
	ax.moveSpeedRW(32,300,650)
	ax.moveSpeedRW(23,600,650)
	ax.moveSpeedRW(33,600,650)

	ax.action()
	sleep(_DELAY)

#	ax.moveSpeedRW(21,300,650)
#	ax.moveSpeedRW(31,700,650)
	ax.moveSpeedRW(22,700,650)
	ax.moveSpeedRW(32,700,650)
	ax.moveSpeedRW(23,300,650)
	ax.moveSpeedRW(33,300,650)
		
	ax.action()
	sleep(_DELAY)

try:
	while True :
		move()
except KeyboardInterrupt :
	list = ax.learnServos(10,64)
	for i in range(0, len(list)) :
		servo = list[i]
		ax.move(servo, 512)
		sleep(0.1)

