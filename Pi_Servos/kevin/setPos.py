#!/usr/bin/python
from ax import Ax12
from time import sleep
import os

ax = Ax12()
list = ax.learnServos(10,64)
_FACTOR = 0.29296875 #300/1024 -> omrekenfactor van graden naar stappen

def rest(legNr) :
	loc = [0,0,0]
	if legNr == 1 :
		loc[1] = 42.37
		loc[2] = 137.17
	elif legNr == 2 :
		loc[1] = 40.68
		loc[2] = 120
	elif legNr == 3 : 
		loc[1] = 42.37
		loc[2] = 137.17
	elif legNr == 4 :
		loc[1] = 34.86
		loc[2] = 137.17
	elif legNr == 5 :
		loc[1] = 40.68 - 1.81
		loc[2] = 120 + 8.49
	elif legNr == 6 :
		loc[1] = 34.86
		loc[2] = 137.17

	#ready positions
	ax.moveSpeed(10*legNr+1, int(512 + (loc[0]/_FACTOR)), 512)
	ax.moveSpeed(10*legNr+2, int(512 + (loc[1]/_FACTOR)), 512)
	ax.moveSpeed(10*legNr+3, int(512 + (loc[2]/_FACTOR)), 512)
	
for legNr in range (1,7) :	
	rest(legNr)
	ax.action() # TODO do this here?
	sleep(0.2)
	
	
