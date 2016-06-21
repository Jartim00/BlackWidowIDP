#!/usr/bin/python
from ax import Ax12
from time import sleep
import servospeedcalculator as sc
import os, sys
ax = Ax12()

## bring the spider to a stable starting stand
def startPosition(tel):
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
def walk(tel):
	for x in range(0, 4):
		sc.moveInTimeRW(12, 750, tel)
		sc.moveInTimeRW(13, 880, tel)
		sc.moveInTimeRW(32, 750, tel)
		sc.moveInTimeRW(33, 880, tel)
		sc.moveInTimeRW(52, 750, tel)
		sc.moveInTimeRW(53, 880, tel)
		ax.action()
		sleep(tel)
		
		sc.moveInTimeRW(12, 620, tel)
		sc.moveInTimeRW(32, 620, tel)
		sc.moveInTimeRW(52, 620, tel)
		ax.action()
		sleep(tel)
		
		sc.moveInTimeRW(22, 750, tel)
		sc.moveInTimeRW(23, 880, tel)
		sc.moveInTimeRW(42, 750, tel)
		sc.moveInTimeRW(43, 880, tel)
		sc.moveInTimeRW(62, 750, tel)
		sc.moveInTimeRW(63, 880, tel)
		ax.action()
		sleep(tel)
		
		sc.moveInTimeRW(22, 620, tel)
		sc.moveInTimeRW(42, 620, tel)
		sc.moveInTimeRW(62, 620, tel)
		ax.action()
		sleep(tel)
	
		x += 1
	
## raise the front end of the body 	
def raiseHead(tel):
	#tel 40,41
	sc.moveInTimeRW(11, 350, 2*tel)
	sc.moveInTimeRW(12, 450, 2*tel)
	sc.moveInTimeRW(13, 780, 2*tel)
	
	sc.moveInTimeRW(21, 520, 2*tel)
	sc.moveInTimeRW(22, 500, 2*tel)
	sc.moveInTimeRW(23, 900, 2*tel)
	
	sc.moveInTimeRW(31, 512, 2*tel)
	sc.moveInTimeRW(32, 720, 2*tel)
	sc.moveInTimeRW(33, 1020, 2*tel)
	
	sc.moveInTimeRW(41, 512, 2*tel)
	sc.moveInTimeRW(42, 720, 2*tel)
	sc.moveInTimeRW(43, 1020, 2*tel)
	
	sc.moveInTimeRW(51, 520, 2*tel)
	sc.moveInTimeRW(52, 500, 2*tel)
	sc.moveInTimeRW(53, 900, 2*tel)
	
	sc.moveInTimeRW(61, 670, 2*tel)
	sc.moveInTimeRW(62, 450, 2*tel)
	sc.moveInTimeRW(63, 780, 2*tel)
	
	ax.action()
	sleep(2*tel)
	
	#tel 42,43
	sc.moveInTimeRW(11, 350, 2*tel)
	sc.moveInTimeRW(12, 720, 2*tel)
	sc.moveInTimeRW(13, 1020, 2*tel)
	
	sc.moveInTimeRW(21, 520, 2*tel)
	sc.moveInTimeRW(22, 720, 2*tel)
	sc.moveInTimeRW(23, 1020, 2*tel)
	
	sc.moveInTimeRW(31, 670, 2*tel)
	sc.moveInTimeRW(32, 720, 2*tel)
	sc.moveInTimeRW(33, 1020, 2*tel)
	
	sc.moveInTimeRW(41, 350, 2*tel)
	sc.moveInTimeRW(42, 720, 2*tel)
	sc.moveInTimeRW(43, 1020, 2*tel)
	
	sc.moveInTimeRW(51, 520, 2*tel)
	sc.moveInTimeRW(52, 720, 2*tel)
	sc.moveInTimeRW(53, 1020, 2*tel)
	
	sc.moveInTimeRW(61, 670, 2*tel)
	sc.moveInTimeRW(62, 720, 2*tel)
	sc.moveInTimeRW(63, 1020, 2*tel)
	
	ax.action()

## raise the body
def raiseBody(tel):
	#tel 44 t/m 47
	sc.moveInTimeRW(11, 350, 4*tel)
	sc.moveInTimeRW(12, 400, 4*tel)
	sc.moveInTimeRW(13, 700, 4*tel)
	
	sc.moveInTimeRW(21, 520, 4*tel)
	sc.moveInTimeRW(22, 400, 4*tel)
	sc.moveInTimeRW(23, 700, 4*tel)
	
	sc.moveInTimeRW(31, 670, 4*tel)
	sc.moveInTimeRW(32, 400, 4*tel)
	sc.moveInTimeRW(33, 700, 4*tel)
	
	sc.moveInTimeRW(41, 350, 4*tel)
	sc.moveInTimeRW(42, 400, 4*tel)
	sc.moveInTimeRW(43, 700, 4*tel)
	
	sc.moveInTimeRW(51, 520, 4*tel)
	sc.moveInTimeRW(52, 400, 4*tel)
	sc.moveInTimeRW(53, 700, 4*tel)
	
	sc.moveInTimeRW(61, 670, 4*tel)
	sc.moveInTimeRW(62, 400, 4*tel)
	sc.moveInTimeRW(63, 700, 4*tel)
	
	ax.action()
	sleep(4*tel)

	#tel 48 t/m 51
	sc.moveInTimeRW(11, 350, 4*tel)
	sc.moveInTimeRW(12, 720, 4*tel)
	sc.moveInTimeRW(13, 1020, 4*tel)
	
	sc.moveInTimeRW(21, 520, 4*tel)
	sc.moveInTimeRW(22, 720, 4*tel)
	sc.moveInTimeRW(23, 1020, 4*tel)
	
	sc.moveInTimeRW(31, 670, 4*tel)
	sc.moveInTimeRW(32, 720, 4*tel)
	sc.moveInTimeRW(33, 1020, 4*tel)
	
	sc.moveInTimeRW(41, 350, 4*tel)
	sc.moveInTimeRW(42, 720, 4*tel)
	sc.moveInTimeRW(43, 1020, 4*tel)
	
	sc.moveInTimeRW(51, 520, 4*tel)
	sc.moveInTimeRW(52, 720, 4*tel)
	sc.moveInTimeRW(53, 1020, 4*tel)
	
	sc.moveInTimeRW(61, 670, 4*tel)
	sc.moveInTimeRW(62, 720, 4*tel)
	sc.moveInTimeRW(63, 1020, 4*tel)
	
	ax.action()

## make a rainbow movement with the front paws
def rainbow(tel):
	#tel 52,53
	sc.moveInTimeRW(11, 720, 2*tel)
	sc.moveInTimeRW(12, 720, 2*tel)
	sc.moveInTimeRW(13, 505, 2*tel)
	
	sc.moveInTimeRW(21, 600, 2*tel)
	sc.moveInTimeRW(22, 500, 2*tel)
	sc.moveInTimeRW(23, 900, 2*tel)
	
	sc.moveInTimeRW(51, 300, 2*tel)
	sc.moveInTimeRW(52, 500, 2*tel)
	sc.moveInTimeRW(53, 900, 2*tel)
	
	sc.moveInTimeRW(61, 300, 2*tel)
	sc.moveInTimeRW(62, 720, 2*tel)
	sc.moveInTimeRW(63, 505, 2*tel)
	
	ax.action()
	sleep(2*tel)
	
	#tel 54,55
	sc.moveInTimeRW(11, 370, 2*tel)
	sc.moveInTimeRW(12, 720, 2*tel)
	sc.moveInTimeRW(13, 505, 2*tel)
	
	sc.moveInTimeRW(21, 520, 2*tel)
	sc.moveInTimeRW(22, 500, 2*tel)
	sc.moveInTimeRW(23, 900, 2*tel)
	
	sc.moveInTimeRW(51, 520, 2*tel)
	sc.moveInTimeRW(52, 500, 2*tel)
	sc.moveInTimeRW(53, 900, 2*tel)
	
	sc.moveInTimeRW(61, 655, 2*tel)
	sc.moveInTimeRW(62, 720, 2*tel)
	sc.moveInTimeRW(63, 505, 2*tel)
	
	ax.action()
	sleep(2*tel)
	
	#tel 56,57
	sc.moveInTimeRW(11, 350, 2*tel)
	sc.moveInTimeRW(12, 620, 2*tel)
	sc.moveInTimeRW(13, 880, 2*tel)
	
	sc.moveInTimeRW(21, 520, 2*tel)
	sc.moveInTimeRW(22, 720, 2*tel)
	sc.moveInTimeRW(23, 1020, 2*tel)
	
	sc.moveInTimeRW(51, 520, 2*tel)
	sc.moveInTimeRW(52, 720, 2*tel)
	sc.moveInTimeRW(53, 1020, 2*tel)
	
	sc.moveInTimeRW(61, 670, 2*tel)
	sc.moveInTimeRW(62, 620, 2*tel)
	sc.moveInTimeRW(63, 880, 2*tel)
	
	ax.action()
	
## make 1 1/4 pirouette
def pirouette(tel):
	#poot omhoog
	sc.moveInTimeRW(12, 750, 0.33*tel)
	sc.moveInTimeRW(13, 880, 0.33*tel)
	sc.moveInTimeRW(32, 750, 0.33*tel)
	sc.moveInTimeRW(33, 880, 0.33*tel)
	sc.moveInTimeRW(52, 750, 0.33*tel)
	sc.moveInTimeRW(53, 880, 0.33*tel)
	ax.action()
	sleep(0.33*tel)
	
	#draai
	sc.moveInTime(11, 670, 0.33*tel)
	sc.moveInTime(31, 670, 0.33*tel)
	sc.moveInTime(51, 600, 0.33*tel)
	ax.action()
	sleep(0.33*tel)
	
	x = 0
	
	for x in range(0, 8):
		#poot omlaag
		sc.moveInTimeRW(12, 620, 0.33*tel)
		sc.moveInTimeRW(32, 620, 0.33*tel)
		sc.moveInTimeRW(52, 620, 0.33*tel)
		ax.action()
		sleep(0.33*tel)
		
		#poot omhoog
		sc.moveInTimeRW(22, 750, 0.33*tel)
		sc.moveInTimeRW(23, 880, 0.33*tel)
		sc.moveInTimeRW(42, 750, 0.33*tel)
		sc.moveInTimeRW(43, 880, 0.33*tel)
		sc.moveInTimeRW(62, 750, 0.33*tel)
		sc.moveInTimeRW(63, 880, 0.33*tel)
		ax.action()
		sleep(0.33*tel)
		
		#draai lichaam
		sc.moveInTime(11, 512, 0.33*tel)
		sc.moveInTime(31, 512, 0.33*tel)
		sc.moveInTime(51, 512, 0.33*tel)
		
		sc.moveInTime(21, 600, 0.33*tel)
		sc.moveInTime(41, 670, 0.33*tel)
		sc.moveInTime(61, 670, 0.33*tel)
		ax.action()
		sleep(0.33*tel)
		
		#poot omlaag
		sc.moveInTimeRW(22, 620, 0.33*tel)
		sc.moveInTimeRW(42, 620, 0.33*tel)
		sc.moveInTimeRW(62, 620, 0.33*tel)
		ax.action()
		sleep(0.33*tel)
		
		#poot omhoog
		sc.moveInTimeRW(12, 750, 0.33*tel)
		sc.moveInTimeRW(13, 880, 0.33*tel)
		sc.moveInTimeRW(32, 750, 0.33*tel)
		sc.moveInTimeRW(33, 880, 0.33*tel)
		sc.moveInTimeRW(52, 750, 0.33*tel)
		sc.moveInTimeRW(53, 880, 0.33*tel)
		ax.action()
		sleep(0.33*tel)
		
		#draai lichaam
		sc.moveInTime(21, 512, 0.33*tel)
		sc.moveInTime(41, 512, 0.33*tel)
		sc.moveInTime(61, 512, 0.33*tel)
		
		sc.moveInTime(11, 670, 0.33*tel)
		sc.moveInTime(31, 670, 0.33*tel)
		sc.moveInTime(51, 600, 0.33*tel)
		ax.action()
		sleep(0.33*tel)
	
	#poot omlaag
	sc.moveInTimeRW(12, 620, 0.33*tel)
	sc.moveInTimeRW(32, 620, 0.33*tel)
	sc.moveInTimeRW(52, 620, 0.33*tel)
	ax.action()
	sleep(0.33*tel)
	
	#poot omhoog
	sc.moveInTimeRW(22, 750, 0.33*tel)
	sc.moveInTimeRW(23, 880, 0.33*tel)
	sc.moveInTimeRW(42, 750, 0.33*tel)
	sc.moveInTimeRW(43, 880, 0.33*tel)
	sc.moveInTimeRW(62, 750, 0.33*tel)
	sc.moveInTimeRW(63, 880, 0.33*tel)
	ax.action()
	sleep(0.33*tel)
	
	#draai lichaam
	sc.moveInTime(11, 512, 0.33*tel)
	sc.moveInTime(31, 512, 0.33*tel)
	sc.moveInTime(51, 512, 0.33*tel)
	
	sc.moveInTime(21, 600, 0.33*tel)
	sc.moveInTime(41, 670, 0.33*tel)
	sc.moveInTime(61, 670, 0.33*tel)
	ax.action()
	sleep(0.33*tel)
	
	#poot omlaag
	sc.moveInTimeRW(22, 620, 0.33*tel)
	sc.moveInTimeRW(42, 620, 0.33*tel)
	sc.moveInTimeRW(62, 620, 0.33*tel)
	ax.action()
	sleep(0.33*tel)
	
	sleep(0.18*tel) #tijd vullen als je op stukjes tel uitkomt.
	startPosition(0.5*tel)