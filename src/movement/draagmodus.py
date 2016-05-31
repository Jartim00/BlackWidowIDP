#!/usr/bin/python
from ax import Ax12
from time import sleep

ax = Ax12()

#afwachten op Controller voor input zodat draagmodus kan worden geactiveerd




def upper1(): #servo 11,12,13
	ax.move(11,512)
	sleep(0.04)
	ax.move(13,935)
	sleep(0.04)
	ax.move(12,667)
	sleep(0.04)

def upper2(): #servo 61,62,63
	ax.move(61,512)
	sleep(0.04)
	ax.move(63,935)
	sleep(0.04)
	ax.move(62,667)
	sleep(0.04)

def mid1(): #servo 21,22,23
	ax.move(21,512)
	sleep(0.04)
	ax.move(23,935)
	sleep(0.04)
	ax.move(22,667)
	sleep(0.04)

def mid2(): #servo 51,52,53
	ax.move(51,512)
	sleep(0.04)
	ax.move(53,935)
	sleep(0.04)
	ax.move(52,667)
	sleep(0.04)	

def lower1(): #servo 31,32,33
	ax.move(31,512)
	sleep(0.04)
	ax.move(33,935)
	sleep(0.04)
	ax.move(32,667)
	sleep(0.04)

def lower2(): #servo 41,42,43
	ax.move(41,512)
	sleep(0.04)
	ax.move(43,935)
	sleep(0.04)
	ax.move(42,667)
	sleep(0.04)

def samen():
	upper1()
	upper2()
	sleep(0.5)
	mid1()
	mid2()
	sleep(0.5)
	lower1()
	lower2()
	sleep(0.5)

samen()




#upper1		 upper2
#13-12-11|	|61-62-63#
#
#mid1		 mid2
#23-22-21|	|51-52-53#
#
#lower1		 lower2
#33-32-31|	|41-42-43#

