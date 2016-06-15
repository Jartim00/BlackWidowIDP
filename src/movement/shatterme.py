#!/usr/bin/python
from ax import Ax12
from time import sleep
import servospeedcalculator as sc
import os, sys
import specialmoves as special
ax = Ax12()

tel = 0.8278

stop = False

## changes the stop boolean to true so the dance function will stop
def stop():
	global stop
	stop = True
	
## the complete dance
# @return this is only there to break out of the function
def showMeHowGoodYourDancingIs():
	#tel 1,2,3
	special.startPosition()
	sleep(3*tel)
	if stop: return
	
	#----blok1----
	
	#tel 4 t/m 19 -> 13.2448 sec
	#special.walk()
	sleep(16*tel)
	if stop: return
	
	#----blok2----
	
	#tel 20,21
	sc.moveInTimeRW(31, 670, 2*tel)
	sc.moveInTimeRW(32, 818, 2*tel)
	sc.moveInTimeRW(33, 1020, 2*tel)
	ax.action()
	sleep(2*tel)
	if stop: return
	
	#tel 22,23
	sc.moveInTimeRW(41, 350, 2*tel)
	sc.moveInTimeRW(42, 818, 2*tel)
	sc.moveInTimeRW(43, 1020, 2*tel)
	ax.action()
	sleep(2*tel)
	if stop: return
	
	#tel 24,25
	sc.moveInTimeRW(21, 520, 2*tel)
	sc.moveInTimeRW(22, 818, 2*tel)
	sc.moveInTimeRW(23, 1020, 2*tel)
	ax.action()
	sleep(2*tel)
	if stop: return
	
	#tel 26,27
	sc.moveInTimeRW(51, 520, 2*tel)
	sc.moveInTimeRW(52, 818, 2*tel)
	sc.moveInTimeRW(53, 1020, 2*tel)
	ax.action()
	sleep(2*tel)
	if stop: return
	
	#tel 28
	sc.moveInTimeRW(11, 350, tel)
	sc.moveInTimeRW(12, 512, tel)
	sc.moveInTimeRW(13, 512, tel)
	ax.action()
	sleep(tel)
	if stop: return
	
	#tel 29
	sc.moveInTimeRW(11, 350, tel)
	sc.moveInTimeRW(12, 725, tel)
	sc.moveInTimeRW(13, 512, tel)
	ax.action()
	sleep(tel)
	if stop: return
	
	#tel 30
	sc.moveInTimeRW(11, 350, tel)
	sc.moveInTimeRW(12, 512, tel)
	sc.moveInTimeRW(13, 512, tel)
	ax.action()
	sleep(tel)
	if stop: return
	
	#tel 31
	sc.moveInTimeRW(11, 350, tel)
	sc.moveInTimeRW(12, 620, tel)
	sc.moveInTimeRW(13, 880, tel)
	ax.action()
	sleep(tel)
	if stop: return
	
	#tel 32
	sc.moveInTimeRW(61, 670, tel)
	sc.moveInTimeRW(62, 512, tel)
	sc.moveInTimeRW(63, 512, tel)
	ax.action()
	sleep(tel)
	if stop: return
	
	#tel 33
	sc.moveInTimeRW(61, 670, tel)
	sc.moveInTimeRW(62, 725, tel)
	sc.moveInTimeRW(63, 512, tel)
	ax.action()
	sleep(tel)
	if stop: return
	
	#tel 34
	sc.moveInTimeRW(61, 670, tel)
	sc.moveInTimeRW(62, 512, tel)
	sc.moveInTimeRW(63, 512, tel)
	ax.action()
	sleep(tel)
	if stop: return
	
	#tel 35
	sc.moveInTimeRW(61, 670, tel)
	sc.moveInTimeRW(62, 620, tel)
	sc.moveInTimeRW(63, 880, tel)
	ax.action()
	sleep(tel)
	if stop: return
	
	#tel 36,37
	sc.moveInTimeRW(11, 350, 2*tel)
	sc.moveInTimeRW(12, 818, 2*tel)
	sc.moveInTimeRW(13, 1020, 2*tel)
	ax.action()
	sleep(2*tel)
	if stop: return
	
	#tel 38,39
	sc.moveInTimeRW(61, 670, 2*tel)
	sc.moveInTimeRW(62, 818, 2*tel)
	sc.moveInTimeRW(63, 1020, 2*tel)
	ax.action()
	sleep(2*tel)
	if stop: return
	
	#tel 40 t/m 43
	special.raiseHead()
	sleep(2*tel)
	if stop: return
	
	#tel 44 t/m 51
	special.raiseBody()
	sleep(4*tel)
	if stop: return
	
	#----blok3----
	
	#tel 52 t/m 57
	special.rainbow()
	sleep(2*tel)
	if stop: return
	
	#tel 58,59
	sc.moveInTimeRW(21, 520, 2*tel)
	sc.moveInTimeRW(22, 620, 2*tel)
	sc.moveInTimeRW(23, 880, 2*tel)
	ax.action()
	sleep(2*tel)
	if stop: return
	
	#tel 60,61
	sc.moveInTimeRW(51, 520, 2*tel)
	sc.moveInTimeRW(52, 620, 2*tel)
	sc.moveInTimeRW(53, 880, 2*tel)
	ax.action()
	sleep(2*tel)
	if stop: return
	
	#tel 62
	sc.moveInTimeRW(21, 512, tel)
	sc.moveInTimeRW(22, 512, tel)
	sc.moveInTimeRW(23, 512, tel)
	
	sc.moveInTimeRW(51, 512, tel)
	sc.moveInTimeRW(52, 512, tel)
	sc.moveInTimeRW(53, 512, tel)
	
	ax.action()
	sleep(tel)
	if stop: return
	
	#tel 63,64,65
	sc.moveInTimeRW(21, 512, 3*tel)
	sc.moveInTimeRW(22, 750, 3*tel)
	sc.moveInTimeRW(23, 512, 3*tel)
	
	sc.moveInTimeRW(51, 512, 3*tel)
	sc.moveInTimeRW(52, 750, 3*tel)
	sc.moveInTimeRW(53, 512, 3*tel)
	
	ax.action()
	sleep(3*tel)
	if stop: return
	
	#tel 66
	sc.moveInTimeRW(23, 880, tel)
	sc.moveInTimeRW(53, 880, tel)
	ax.action()
	sleep(tel)
	if stop: return
	
	#tel 67
	sc.moveInTimeRW(22, 620, tel)
	sc.moveInTimeRW(52, 620, tel)
	ax.action()
	sleep(tel)
	if stop: return
	
	#tel 68,69
	sc.moveInTimeRW(31, 670, 2*tel)
	sc.moveInTimeRW(32, 620, 2*tel)
	sc.moveInTimeRW(33, 880, 2*tel)
	ax.action()
	sleep(2*tel)
	if stop: return
	
	#tel 70,71
	sc.moveInTimeRW(41, 350, tel)
	sc.moveInTimeRW(42, 620, tel)
	sc.moveInTimeRW(43, 880, tel)
	ax.action()
	sleep(2*tel)
	if stop: return
	
	#tel 72 t/m 83 -> 9.9336 sec
	#special.pirouette()
	if stop: return
	
if __name__ == "__main__":
	showMeHowGoodYourDancingIs()
	
#moveInTimeRW(id,endPos,time)
#ax.action()
#sleep(sec)
#if stop: return