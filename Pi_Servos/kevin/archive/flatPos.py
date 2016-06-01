#!/usr/bin/python
from ax12 import Ax12
from time import sleep
import os

ax = Ax12()
list = ax.learnServos(10,64)
print list

for i in range(0, len(list)) :
	servo = list[i]
	ax.move(servo, 512)
	sleep(0.1)
