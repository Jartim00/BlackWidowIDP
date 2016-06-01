#!/usr/bin/python
from ax import Ax12
from time import sleep
import os

class vooruit:
	ax = Ax12()

	def vooruit(self):
		self.ax.move(61,674)
		self.ax.move(11,350)
		sleep(0.4)
		self.ax.move(61,512)
		self.ax.move(11,512)
		sleep(0.4)

	def rechts(self):
		self.ax.move(11,512)
		sleep(0.4)
		self.ax.move(11,674)
		sleep(0.4)

	def links(self):
		self.ax.move(61,674)
		sleep(0.4)
		self.ax.move(61,512)
		sleep(0.4)

	def rust(self):
		self.upper1()
		self.upper2()
		sleep(0.5)
		self.mid1()
		self.mid2()
		sleep(0.5)
		self.lower1()
		self.lower2()
		sleep(0.5)

	def upper1(self): #servo 11,12,13
		self.ax.move(11,512)
		sleep(0.04)
		self.ax.move(13,935)
		sleep(0.04)
		self.ax.move(12,667)
		sleep(0.04)

	def upper2(self): #servo 61,62,63
		self.ax.move(61,512)
		sleep(0.04)
		self.ax.move(63,935)
		sleep(0.04)
		self.ax.move(62,667)
		sleep(0.04)

	def mid1(self): #servo 21,22,23
		self.ax.move(21,512)
		sleep(0.04)
		self.ax.move(23,935)
		sleep(0.04)
		self.ax.move(22,667)
		sleep(0.04)

	def mid2(self): #servo 51,52,53
		self.ax.move(51,512)
		sleep(0.04)
		self.ax.move(53,935)
		sleep(0.04)
		self.ax.move(52,667)
		sleep(0.04)	

	def lower1(self): #servo 31,32,33
		self.ax.move(31,512)
		sleep(0.04)
		self.ax.move(33,935)
		sleep(0.04)
		self.ax.move(32,667)
		sleep(0.04)

	def lower2(self): #servo 41,42,43
		self.ax.move(41,512)
		sleep(0.04)
		self.ax.move(43,935)
		sleep(0.04)
		self.ax.move(42,667)
		sleep(0.04)





