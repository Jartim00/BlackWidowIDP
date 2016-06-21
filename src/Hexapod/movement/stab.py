#!/usr/bin/python
from ax import Ax12
from time import sleep
import time


ax = Ax12()
class Stabby:
	a = 512.0/60.0
	z = 35.0/60.0
	omrek = a*z
	def setAttackMode(self):
		ax.moveSpeedRW(21,574,350)
		ax.moveSpeedRW(31,350,350)
		ax.moveSpeedRW(41,674,350)
		ax.moveSpeedRW(51,450,350)
		ax.moveSpeedRW(22,650,350)
		ax.moveSpeedRW(32,774,350)
		ax.moveSpeedRW(42,774,350)
		ax.moveSpeedRW(52,650,350)
		ax.moveSpeedRW(23,1000,350)
		ax.moveSpeedRW(33,1000,350)
		ax.moveSpeedRW(43,1000,350)
		ax.moveSpeedRW(53,1000,350)
		ax.action()
		sleep(0.9)

	def setStabPos(self):
		ax.moveSpeedRW(63,512,500)
		ax.moveSpeedRW(13,512,500)
		ax.moveSpeedRW(12,600,200)
		ax.moveSpeedRW(62,600,200)
		ax.moveSpeedRW(11,512,350)
		ax.moveSpeedRW(61,512,350)
		ax.action()
		sleep(0.1)

	def stab(self):
		ax.moveSpeedRW(61,350,350)
		ax.moveSpeedRW(11,674,350)
		ax.action()
		sleep(0.2)

	def returning(self):
		ax.moveSpeedRW(61,512,350)
		ax.moveSpeedRW(11,512,350)
		ax.action()
		sleep(0.1)

	def gyroSens(self,b):
		if b < -10 or b > 60:
			raise Exception("Out of bounds")
		ax.moveSpeedRW(12,511+int(Stabby.omrek*int(b)),350)
		ax.moveSpeedRW(62,511+int(Stabby.omrek*int(b)),350)
		ax.action()



#bx = Stabby()
#bx.setAttackMode()
#bx.setStabPos()
#sleep(0.7)
#bx.stab()
#sleep(0.2)
#bx.returning()
#bx.gyroSens(80)
