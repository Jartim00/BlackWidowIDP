#!/usr/bin/python
from ax import Ax12
from time import sleep
import servospeedcalculator as sc
import os, sys
import specialmoves as special
ax = Ax12()
class Dance(object):
	tel0 = 0.8416
	tel1 = 0.8126
	tel2 = 0.81
	tel3 = 0.84
	tel4 = 0.85
	tel5 = 0.8313
	tel6 = 0.825
	tel7 = 0.8349

	stop = False

	## the complete dance
	# @return this is only there to break out of the function
	def showMeHowGoodYourDancingIs():
		#tel 1,2,3
		special.startPosition(tel0)
		sleep(5*tel0)
		if stop: return

		#----blok1----
		blok1(tel1)
		if stop: return

		#----blok2----
		blok2(tel2)
		if stop: return

		#----blok3----
		blok3(tel3)
		if stop: return

		#----blok4----
		#blok4(tel4)
		if stop: return

		#----blok5----
		blok5(tel5)
		if stop: return

		#----blok6----
		blok6(tel6)
		if stop: return

		#----blok7----
		#blok7(tel7)
		if stop: return

		sleep(5*tel)
		special.startPosition()

	def blok1(tel):
		#tel 4 t/m 19
		special.walk(tel)
		if stop: return

	def blok2(tel):
		#tel 20,21
		sc.moveInTimeRW(31, 670, 2*tel)
		sc.moveInTimeRW(32, 720, 2*tel)
		sc.moveInTimeRW(33, 1020, 2*tel)
		ax.action()
		sleep(2*tel)
		if stop: return

		#tel 22,23
		sc.moveInTimeRW(41, 350, 2*tel)
		sc.moveInTimeRW(42, 720, 2*tel)
		sc.moveInTimeRW(43, 1020, 2*tel)
		ax.action()
		sleep(2*tel)
		if stop: return

		#tel 24,25
		sc.moveInTimeRW(21, 520, 2*tel)
		sc.moveInTimeRW(22, 720, 2*tel)
		sc.moveInTimeRW(23, 1020, 2*tel)
		ax.action()
		sleep(2*tel)
		if stop: return

		#tel 26,27
		sc.moveInTimeRW(51, 520, 2*tel)
		sc.moveInTimeRW(52, 720, 2*tel)
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
		sc.moveInTimeRW(12, 720, 2*tel)
		sc.moveInTimeRW(13, 1020, 2*tel)
		ax.action()
		sleep(2*tel)
		if stop: return

		#tel 38,39
		sc.moveInTimeRW(61, 670, 2*tel)
		sc.moveInTimeRW(62, 720, 2*tel)
		sc.moveInTimeRW(63, 1020, 2*tel)
		ax.action()
		sleep(2*tel)
		if stop: return

		#tel 40 t/m 43
		special.raiseHead(tel)
		sleep(2*tel)
		if stop: return

		#tel 44 t/m 51
		special.raiseBody(tel)
		sleep(4*tel)
		if stop: return

	def blok3(tel):
		#tel 52 t/m 57
		special.rainbow(tel)
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
		sc.moveInTimeRW(23, 880, 0.5*tel)
		sc.moveInTimeRW(53, 880, 0.5*tel)
		ax.action()
		sleep(0.5*tel)
		if stop: return

		sc.moveInTimeRW(22, 620, 0.5*tel)
		sc.moveInTimeRW(52, 620, 0.5*tel)
		ax.action()
		sleep(0.5*tel)
		if stop: return

		#tel 67 t/m 84
		special.pirouette(tel)
		if stop: return

	#def blok4(tel):
		#tel 85
		# sc.moveInTimeRW(11, 512, 0.5*tel)
		# sc.moveInTimeRW(12, 620, 0.5*tel)
		# sc.moveInTimeRW(13, 880, 0.5*tel)

		# sc.moveInTimeRW(21, 600, 0.5*tel)
		# sc.moveInTimeRW(22, 500, 0.5*tel)
		# sc.moveInTimeRW(23, 900, 0.5*tel)

		# sc.moveInTimeRW(31, 512, 0.5*tel)
		# sc.moveInTimeRW(32, 620, 0.5*tel)
		# sc.moveInTimeRW(33, 880, 0.5*tel)

		# sc.moveInTimeRW(41, 512, 0.5*tel)
		# sc.moveInTimeRW(42, 620, 0.5*tel)
		# sc.moveInTimeRW(43, 880, 0.5*tel)

		# sc.moveInTimeRW(51, 400, 0.5*tel)
		# sc.moveInTimeRW(52, 500, 0.5*tel)
		# sc.moveInTimeRW(53, 900, 0.5*tel)

		# sc.moveInTimeRW(61, 512, 0.5*tel)
		# sc.moveInTimeRW(62, 620, 0.5*tel)
		# sc.moveInTimeRW(63, 880, 0.5*tel)

		# ax.action()
		# sleep(0.5*tel)
		# if stop: return

	def blok5(tel):
		#tel 86
		sc.moveInTimeRW(12, 800, 0.5*tel)
		sc.moveInTimeRW(13, 900, 0.5*tel)

		sc.moveInTimeRW(62, 800, 0.5*tel)
		sc.moveInTimeRW(63, 900, 0.5*tel)

		ax.action()
		sleep(0.5*tel)
		if stop: return

		sc.moveInTimeRW(12, 700, 0.5*tel)
		sc.moveInTimeRW(13, 530, 0.5*tel)

		sc.moveInTimeRW(62, 700, 0.5*tel)
		sc.moveInTimeRW(63, 530, 0.5*tel)

		ax.action()
		sleep(0.5*tel)
		if stop: return

		#tel 87
		special.startPosition(tel)
		sleep(tel)
		if stop: return

		#tel 88,89
		sc.moveInTimeRW(22, 700, 2*tel)
		sc.moveInTimeRW(23, 530, 2*tel)
		ax.action()
		sleep(2*tel)
		if stop: return

		#tel 90,91
		sc.moveInTimeRW(22, 620, 2*tel)
		sc.moveInTimeRW(23, 880, 2*tel)
		ax.action()
		sleep(2*tel)
		if stop: return

		#tel 92,93
		special.startPosition(tel)
		sleep(2*tel)
		if stop: return

		#tel 94
		sc.moveInTimeRW(21, 512, 0.5*tel)
		sc.moveInTimeRW(22, 512, 0.5*tel)
		sc.moveInTimeRW(23, 512, 0.5*tel)
		ax.action()
		sleep(0.5*tel)

		sc.moveInTimeRW(21, 512, 0.5*tel)
		sc.moveInTimeRW(22, 750, 0.5*tel)
		sc.moveInTimeRW(23, 512, 0.5*tel)
		ax.action()
		sleep(0.5*tel)
		if stop: return

		#tel 95
		sc.moveInTimeRW(51, 512, 0.5*tel)
		sc.moveInTimeRW(52, 512, 0.5*tel)
		sc.moveInTimeRW(53, 512, 0.5*tel)
		ax.action()
		sleep(0.5*tel)

		sc.moveInTimeRW(51, 512, 0.5*tel)
		sc.moveInTimeRW(52, 750, 0.5*tel)
		sc.moveInTimeRW(53, 512, 0.5*tel)
		ax.action()
		sleep(0.5*tel)
		if stop: return

		#tel 96
		sc.moveInTimeRW(21, 512, tel)
		sc.moveInTimeRW(22, 512, tel)
		sc.moveInTimeRW(23, 512, tel)

		sc.moveInTimeRW(51, 512, tel)
		sc.moveInTimeRW(52, 512, tel)
		sc.moveInTimeRW(53, 512, tel)

		ax.action()
		sleep(tel)

		#tel 97
		sc.moveInTimeRW(22, 620, tel)
		sc.moveInTimeRW(23, 880, tel)
		sc.moveInTimeRW(52, 620, tel)
		sc.moveInTimeRW(53, 880, tel)
		ax.action()
		sleep(tel)
		if stop: return

		#tel 98,99,100
		special.startPosition(tel)
		sleep(3*tel)
		if stop: return

		#tel 101
		sc.moveInTimeRW(11, 512, tel)
		sc.moveInTimeRW(12, 620, tel)
		sc.moveInTimeRW(13, 880, tel)

		sc.moveInTimeRW(21, 600, tel)
		sc.moveInTimeRW(22, 500, tel)
		sc.moveInTimeRW(23, 900, tel)

		sc.moveInTimeRW(31, 512, tel)
		sc.moveInTimeRW(32, 620, tel)
		sc.moveInTimeRW(33, 880, tel)

		sc.moveInTimeRW(41, 512, tel)
		sc.moveInTimeRW(42, 620, tel)
		sc.moveInTimeRW(43, 880, tel)

		sc.moveInTimeRW(51, 400, tel)
		sc.moveInTimeRW(52, 500, tel)
		sc.moveInTimeRW(53, 900, tel)

		sc.moveInTimeRW(61, 512, tel)
		sc.moveInTimeRW(62, 620, tel)
		sc.moveInTimeRW(63, 880, tel)

		ax.action()
		sleep(tel)
		if stop: return

		#tel 102
		sc.moveInTimeRW(61, 350, tel)
		sc.moveInTimeRW(62, 512, tel)
		sc.moveInTimeRW(63, 512, tel)
		ax.action()
		sleep(tel)
		if stop: return

		#tel 103,104
		sc.moveInTimeRW(63, 650, 2*tel)
		ax.action()
		sleep(2*tel)
		if stop: return

		#tel 105
		sc.moveInTimeRW(11, 670, tel)
		sc.moveInTimeRW(12, 512, tel)
		sc.moveInTimeRW(13, 512, tel)
		ax.action()
		sleep(tel)
		if stop: return

		#tel 106
		sc.moveInTimeRW(13, 650, tel)
		ax.action()
		sleep(tel)
		if stop: return

		#tel 107
		sc.moveInTimeRW(61, 350, tel)
		sc.moveInTimeRW(62, 512, tel)
		sc.moveInTimeRW(63, 512, tel)

		sc.moveInTimeRW(11, 670, tel)
		sc.moveInTimeRW(12, 512, tel)
		sc.moveInTimeRW(13, 512, tel)

		ax.action()
		sleep(tel)
		if stop: return

		#tel 108,109
		sc.moveInTimeRW(62, 620, tel)
		sc.moveInTimeRW(63, 880, tel)

		sc.moveInTimeRW(12, 620, tel)
		sc.moveInTimeRW(13, 880, tel)

		ax.action()
		sleep(tel)
		if stop: return

		#tel 110,111
		sc.moveInTimeRW(61, 670, 2*tel)
		sc.moveInTimeRW(62, 620, 2*tel)
		sc.moveInTimeRW(63, 880, 2*tel)
		ax.action()
		sleep(2*tel)
		if stop: return

		#tel 112,113
		sc.moveInTimeRW(11, 350, 2*tel)
		sc.moveInTimeRW(12, 620, 2*tel)
		sc.moveInTimeRW(13, 880, 2*tel)
		ax.action()
		sleep(2*tel)
		if stop: return

		#tel 114
		special.startPosition(tel)
		sleep(3*tel)
		if stop: return

		#tel 115
		sc.moveInTimeRW(21, 512, tel)
		sc.moveInTimeRW(22, 512, tel)
		sc.moveInTimeRW(23, 512, tel)

		sc.moveInTimeRW(51, 512, tel)
		sc.moveInTimeRW(52, 512, tel)
		sc.moveInTimeRW(53, 512, tel)

		ax.action()
		sleep(tel)

		#tel 116
		sc.moveInTimeRW(22, 620, tel)
		sc.moveInTimeRW(23, 880, tel)
		sc.moveInTimeRW(52, 620, tel)
		sc.moveInTimeRW(53, 880, tel)
		ax.action()
		sleep(tel)
		if stop: return

		#tel 117
		special.startPosition(tel)
		sleep(tel)
		if stop: return

	def blok6(tel):
		#tel 118 t/m 125
		special.raiseBody(tel)
		sleep(3*tel)
		if stop: return

		sleep(8*tel)
		#tel 126


	def blok7(tel):
		sleep(12*tel)

	## changes the stop boolean to true so the dance function will stop
	def stopDans():
		global stop
		stop = True

	if __name__ == "__main__":
		showMeHowGoodYourDancingIs()

	#moveInTimeRW(id,endPos,time)
	#ax.action()
	#sleep(sec)
	#if stop: return
