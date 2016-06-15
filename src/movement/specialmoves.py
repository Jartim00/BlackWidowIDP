#!/usr/bin/python
from ax import Ax12
from time import sleep
import servospeedcalculator as sc
import os, sys
ax = Ax12()

tel = 0.8278

## bring the spider to a stable starting stand
def startPosition():
	#tel 1
	sc.moveInTimeRW(11, 350, tel)
	sc.moveInTimeRW(12, 620, tel)
	sc.moveInTimeRW(13, 880, tel)
	
	sc.moveInTimeRW(21, 520, tel)
	sc.moveInTimeRW(22, 620, tel)
	sc.moveInTimeRW(23, 880, tel)
	
	sc.moveInTimeRW(31, 670, tel)
	sc.moveInTimeRW(32, 620, tel)
	sc.moveInTimeRW(33, 880, tel)
	
	sc.moveInTimeRW(41, 350, tel)
	sc.moveInTimeRW(42, 620, tel)
	sc.moveInTimeRW(43, 880, tel)
	
	sc.moveInTimeRW(51, 520, tel)
	sc.moveInTimeRW(52, 620, tel)
	sc.moveInTimeRW(53, 880, tel)
	
	sc.moveInTimeRW(61, 670, tel)
	sc.moveInTimeRW(62, 620, tel)
	sc.moveInTimeRW(63, 880, tel)
	
	ax.action()
	
## walk for for 16 counts
#def walk():
	
## raise the front end of the body 	
def raiseHead():
	#tel 40,41
	sc.moveInTimeRW(11, 350, 2*tel)
	sc.moveInTimeRW(12, 435, 2*tel)
	sc.moveInTimeRW(13, 710, 2*tel)
	
	sc.moveInTimeRW(21, 520, 2*tel)
	sc.moveInTimeRW(22, 615, 2*tel)
	sc.moveInTimeRW(23, 800, 2*tel)
	
	sc.moveInTimeRW(51, 520, 2*tel)
	sc.moveInTimeRW(52, 615, 2*tel)
	sc.moveInTimeRW(53, 800, 2*tel)
	
	sc.moveInTimeRW(61, 670, 2*tel)
	sc.moveInTimeRW(62, 435, 2*tel)
	sc.moveInTimeRW(63, 710, 2*tel)
	
	ax.action()
	sleep(2*tel)
	
	#tel 42,43
	sc.moveInTimeRW(11, 350, 2*tel)
	sc.moveInTimeRW(12, 818, 2*tel)
	sc.moveInTimeRW(13, 1020, 2*tel)
	
	sc.moveInTimeRW(21, 520, 2*tel)
	sc.moveInTimeRW(22, 818, 2*tel)
	sc.moveInTimeRW(23, 1020, 2*tel)
	
	sc.moveInTimeRW(51, 520, 2*tel)
	sc.moveInTimeRW(52, 818, 2*tel)
	sc.moveInTimeRW(53, 1020, 2*tel)
	
	sc.moveInTimeRW(61, 670, 2*tel)
	sc.moveInTimeRW(62, 818, 2*tel)
	sc.moveInTimeRW(63, 1020, 2*tel)
	
	ax.action()

## raise the body
def raiseBody():
	#tel 44 t/m 47
	sc.moveInTimeRW(11, 350, 2*tel)
	sc.moveInTimeRW(12, 400, 2*tel)
	sc.moveInTimeRW(13, 700, 2*tel)
	
	sc.moveInTimeRW(21, 520, 2*tel)
	sc.moveInTimeRW(22, 400, 2*tel)
	sc.moveInTimeRW(23, 700, 2*tel)
	
	sc.moveInTimeRW(31, 670, 2*tel)
	sc.moveInTimeRW(32, 400, 2*tel)
	sc.moveInTimeRW(33, 700, 2*tel)
	
	sc.moveInTimeRW(41, 350, 2*tel)
	sc.moveInTimeRW(42, 400, 2*tel)
	sc.moveInTimeRW(43, 700, 2*tel)
	
	sc.moveInTimeRW(51, 520, 2*tel)
	sc.moveInTimeRW(52, 400, 2*tel)
	sc.moveInTimeRW(53, 700, 2*tel)
	
	sc.moveInTimeRW(61, 670, 2*tel)
	sc.moveInTimeRW(62, 400, 2*tel)
	sc.moveInTimeRW(63, 700, 2*tel)
	
	ax.action()
	sleep(4*tel)

	#tel 48 t/m 51
	sc.moveInTimeRW(11, 350, 2*tel)
	sc.moveInTimeRW(12, 818, 2*tel)
	sc.moveInTimeRW(13, 1020, 2*tel)
	
	sc.moveInTimeRW(21, 520, 2*tel)
	sc.moveInTimeRW(22, 818, 2*tel)
	sc.moveInTimeRW(23, 1020, 2*tel)
	
	sc.moveInTimeRW(31, 670, 2*tel)
	sc.moveInTimeRW(32, 818, 2*tel)
	sc.moveInTimeRW(33, 1020, 2*tel)
	
	sc.moveInTimeRW(41, 350, 2*tel)
	sc.moveInTimeRW(42, 818, 2*tel)
	sc.moveInTimeRW(43, 1020, 2*tel)
	
	sc.moveInTimeRW(51, 520, 2*tel)
	sc.moveInTimeRW(52, 818, 2*tel)
	sc.moveInTimeRW(53, 1020, 2*tel)
	
	sc.moveInTimeRW(61, 670, 2*tel)
	sc.moveInTimeRW(62, 818, 2*tel)
	sc.moveInTimeRW(63, 1020, 2*tel)
	
	ax.action()

## make a rainbow movement with the front paws
def rainbow():
	#tel 52,53
	sc.moveInTimeRW(11, 720, 2*tel)
	sc.moveInTimeRW(12, 720, 2*tel)
	sc.moveInTimeRW(13, 505, 2*tel)
	
	sc.moveInTimeRW(61, 300, 2*tel)
	sc.moveInTimeRW(62, 720, 2*tel)
	sc.moveInTimeRW(63, 505, 2*tel)
	
	ax.action()
	sleep(2*tel)
	
	#tel 54,55
	sc.moveInTimeRW(11, 370, 2*tel)
	sc.moveInTimeRW(12, 720, 2*tel)
	sc.moveInTimeRW(13, 505, 2*tel)
	
	sc.moveInTimeRW(61, 655, 2*tel)
	sc.moveInTimeRW(62, 720, 2*tel)
	sc.moveInTimeRW(63, 505, 2*tel)
	
	ax.action()
	sleep(2*tel)
	
	#tel 56,57
	sc.moveInTimeRW(11, 350, 2*tel)
	sc.moveInTimeRW(12, 620, 2*tel)
	sc.moveInTimeRW(13, 880, 2*tel)
	
	sc.moveInTimeRW(61, 670, 2*tel)
	sc.moveInTimeRW(62, 620, 2*tel)
	sc.moveInTimeRW(63, 880, 2*tel)
	
	ax.action()
	
## make 1 1/4 pirouette
def pirouette():
	#poot omhoog
	sc.moveInTimeRW(12, 750, tel)
	sc.moveInTimeRW(13, 880, tel)
	sc.moveInTimeRW(32, 750, tel)
	sc.moveInTimeRW(33, 880, tel)
	sc.moveInTimeRW(52, 750, tel)
	sc.moveInTimeRW(53, 880, tel)
	ax.action()
	sleep(tel)
	
	#draai
	sc.moveInTime(11, 300, tel)
	sc.moveInTime(31, 300, tel)
	sc.moveInTime(51, 350, tel)
	ax.action()
	sleep(tel)
	
	x = 0
	
	for x in range(0, 5):
		#poot omlaag
		sc.moveInTimeRW(12, 620, tel)
		sc.moveInTimeRW(32, 620, tel)
		sc.moveInTimeRW(52, 620, tel)
		ax.action()
		sleep(tel)
		
		#poot omhoog
		sc.moveInTimeRW(22, 750, tel)
		sc.moveInTimeRW(23, 880, tel)
		sc.moveInTimeRW(42, 750, tel)
		sc.moveInTimeRW(43, 880, tel)
		sc.moveInTimeRW(62, 750, tel)
		sc.moveInTimeRW(63, 880, tel)
		ax.action()
		sleep(tel)
		
		#draai lichaam
		sc.moveInTime(11, 512, tel)
		sc.moveInTime(31, 512, tel)
		sc.moveInTime(51, 512, tel)
		ax.action()
		sleep(tel)
		
		sc.moveInTime(21, 350, tel)
		sc.moveInTime(41, 300, tel)
		sc.moveInTime(61, 300, tel)
		ax.action()
		sleep(tel)
		
		#poot omlaag
		sc.moveInTimeRW(22, 620, tel)
		sc.moveInTimeRW(42, 620, tel)
		sc.moveInTimeRW(62, 620, tel)
		ax.action()
		sleep(tel)
		
		#poot omhoog
		sc.moveInTimeRW(12, 750, tel)
		sc.moveInTimeRW(13, 880, tel)
		sc.moveInTimeRW(32, 750, tel)
		sc.moveInTimeRW(33, 880, tel)
		sc.moveInTimeRW(52, 750, tel)
		sc.moveInTimeRW(53, 880, tel)
		ax.action()
		sleep(tel)
		
		#draai lichaam
		sc.moveInTime(21, 512, tel)
		sc.moveInTime(41, 512, tel)
		sc.moveInTime(61, 512, tel)
		ax.action()
		sleep(tel)
		
		sc.moveInTime(11, 300, tel)
		sc.moveInTime(31, 300, tel)
		sc.moveInTime(51, 350, tel)
		ax.action()
		sleep(tel)
		
		x += 1