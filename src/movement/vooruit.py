#!/usr/bin/python
from ax import Ax12
from time import sleep
import os

class vooruit:
	ax = Ax12()

	def vooruit(self):
		ax.move(61,674)
		ax.move(11,350)
		sleep(0.4)
		ax.move(61,512)
		ax.move(11,512)
		sleep(0.4)

	def rechts(self):
		ax.move(11,512)
		sleep(0.4)
		ax.move(11,674)
		sleep(0.4)

	def links(self):
		ax.move(61,674)
		sleep(0.4)
		ax.move(61,512)
		sleep(0.4)

	def rust():
		upper1()
		upper2()
		sleep(0.5)
		mid1()
		mid2()
		sleep(0.5)
		lower1()
		lower2()
		sleep(0.5)

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





