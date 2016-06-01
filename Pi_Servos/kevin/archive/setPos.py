#!/usr/bin/python
from ax import Ax12
from time import sleep
import os

ax = Ax12()
list = ax.learnServos(10,64)

for i in range(0, len(list)) :
	servo = list[i]
	if servo%10 == 1 :
		loc = 512
	elif servo%10==2 :
		loc = 750
	elif servo%10 == 3 :
		loc = 1023
	ax.move(servo, loc)
	sleep(0.1)