#!/usr/bin/python
from ax import Ax12
from time import sleep
import os

ax = Ax12()
list = ax.learnServos(10,64)

def time(id, loc) :
	cur = ax.readPosition(id)
	dx = abs(loc - cur) #get the distance to move
	return dx #int(1024 * (dx/140))

for i in range(0, len(list)) :
	servo = list[i]
	if servo%10 == 1 :
		loc = 512
	elif servo%10==2 :
		loc = 90
	elif servo%10 == 3 :
		loc = -45
	ax.moveRW(servo, loc)
	sleep(0.25)
	if(i%6 == 0 ) : 
		ax.action()
