#!/usr/bin/python
from ax import Ax12
from time import sleep
import os

ax = Ax12()
list = ax.learnServos(10,64)
_FACTOR = 0.29296875 #300/1024 -> omrekenfactor van graden naar stappen

#ready positions
	
for legNr in range (1,7) :	
	ax.moveSpeed(10*legNr+1, 512, 512)
	ax.moveSpeed(10*legNr+2, int(512 + (90/_FACTOR)), 512)
	ax.moveSpeed(10*legNr+3, int(512 - (45/_FACTOR)), 512)
	ax.action()
