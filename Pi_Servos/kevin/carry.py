#!/usr/bin/python
from ax import Ax12
ax = Ax12()

## Draagmodus van de spin, waarmee de spin vervoerd en gedragen kan worden.                                                          
def draagmodus():
	_FACTOR = 0.29296875 #300/1024 -> omrekenfactor van graden naar stappen	
	for legNr in range (1,7) :	
		ax.moveSpeed(10*legNr+1, 512, 512)
		ax.moveSpeed(10*legNr+2, int(512 + (90/_FACTOR)), 512)
		ax.moveSpeed(10*legNr+3, int(512 - (45/_FACTOR)), 512)
	ax.action()
