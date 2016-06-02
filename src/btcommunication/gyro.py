#!/usr/bin/python
from ax import Ax12
from time import sleep
import os
import gyro

ax = Ax12()

a = 512/60.0
def gyroSens(b):
	if not -36 <= b <= 35:
		raise IndexError("position should be between -36 and 35")
	ax.moveSpeedRW(12,511+int(a*int(b)),250)
	ax.moveSpeedRW(22,511+int(a*int(b)),250)
	ax.moveSpeedRW(32,511+int(a*int(b)),250)
	sleep(0.04)
	ax.moveSpeedRW(42,511+int(a*int(b)),250)
	ax.moveSpeedRW(52,511+int(a*int(b)),250)
	ax.moveSpeedRW(62,511+int(a*int(b)),250)
	ax.action()


#-36 tot 35 max
#startpunt = 512 is gelijk aan de waarde 0 op basis van input van de gyrosensor
# 0 tot -60, -60 geeft aan dat de positie

#laag = 0 		= -60
#middelpunt= 511 	= 0
#hoog = 1023 		= +60

#512/60.0 = 8.525
#poot hoog is ongeveer 1023-820=203/8.525=24||| 60-24=36
#poot laag is ongeveer 512-200/8.525 = 23,5
