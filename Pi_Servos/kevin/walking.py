#!/usr/bin/python
from ax import Ax12
from time import sleep
#from multiprocessing import Process #not yet being used
#from readValues import readValues, prN, speed #overview screen for information from servo's
import os
ax = Ax12()

debug = True
feet = []

class Foot :
	#has three servo's based on the leg number.
	legNr = 0
	
	def __init__(self, legNr) :
		self.legNr = legNr
		self.lights(True)
		
	def __repr__(self) :
		uhoh = ""
		if self.legNr == 0 :
			uhoh = " (uhoh, no leg number assigned. RED FLAG!)"
		return str(self.legNr) + uhoh
		
	def lights(self, status=True) :
		#zet alle lampjes aan of uit
		ax.setLedStatus(10*self.legNr+1, status)
		ax.setLedStatus(10*self.legNr+2, status)
		ax.setLedStatus(10*self.legNr+3, status)
		
	def step(self, id, deg) :
		_FACTOR = 0.29296875 #300/1024 -> omrekenfactor van graden naar stappen
		step = int(512 + (deg / _FACTOR))
		if step < 0 : return 0
		elif step > 1023 : return 1023
		else : return step
	
	def time(self, id, loc) :
		cur = ax.readPosition(id)
		dx = abs(loc - cur) #get the distance to move
		return dx #int(1024 * (dx/140))
	
	#self: this class. Not needed in call
	#id : servo ID
	#loc: end location
	#spd: speed to use (not used yet, is computed)
	def moveSpeedRW(self, id, loc) :
		loc = self.step(id, loc) #check if valid location
		spd = self.time(id, loc) #make valid time
		if (
			id in ax.learnServos(10,64) #valid servo number
			and loc in range (1024) #valid destination
			and spd in range (1024) #valid speed
		) : 
			ax.moveSpeedRW(id, loc, spd) 
			if debug : print "Servo: " + str(id) + " to loc: " + str(loc) + " at spd: " + str(spd)
		else :
			print "ERROR! moveSpeed(id=" + str(id) + ", loc=" + str(int(loc)) + ", spd=" + str(spd) + ")"
			if not id in ax.learnServos(10,64) :
				print "wrong ID!"
			if not int(loc) in range(1024) :
				print "wrong location!"
			if not spd in range(1024) :
				print "wrong speed!"
		
#	def ready(self) :
#		loc = []
#		#ready-set-go: get into start position (1st half)
#		#move legs 1-3-5 to lift up and cover the distance
#		#move legs 2-4-6 backwards over the floor
#		if self.legNr == 1 :
#			loc[0] = 9.73
#			loc[1] = 5
#		elif self.legNr == 3 :
#			loc[0] = 45 
#			loc[1] = 5
#		elif self.legNr == 5 :
#			loc[0] = -30 
#			loc[1] = 5
#
#		elif self.legNr == 2 :
#			loc[0] = -30
#			loc[1] = 0
#			loc[2] = 0
#		elif self.legNr == 4 :
#			loc[0] = 9.73
#			loc[1] = 0
#			loc[2] = 0
#		elif self.legNr == 6 :
#			loc[0] = 45 
#			loc[1] = 0
#			loc[2] = 0
#
#		self.moveSpeedRW(10*self.legNr+1, loc[0])
#		self.moveSpeedRW(10*self.legNr+2, loc[1])
#		self.moveSpeedRW(10*self.legNr+3, loc[2])
#		
#	def set(self) :
#		return 0
#		loc = []
#		#ready-set-go: get into start position (2nd half)
#		#move legs 1-3-5 to touch down
#		if self.legNr == 1 : loc[1] = -5
#		elif self.legNr == 3 : loc[1] = -5 
#		elif self.legNr == 5 : loc[1] = -5 
#
#		self.moveSpeedRW(10*self.legNr+2, loc[1])

	def go(self) :
		#ready-set-go: get into start position
		print str(self.legNr) + " KNAL MUHAHA!"
		
	def rest(self) :
		loc = [0,0,0]
		if self.legNr == 1 :
			loc[0] = 45 
			loc[1] = 90 #40.68
			loc[2] = -45 #150 #120
		elif self.legNr == 2 :
			loc[0] = 0 
			loc[1] = 90 #40.68
			loc[2] = -45 #150 #120
		elif self.legNr == 3 : 
			loc[0] = -45 
			loc[1] = 90 #40.68
			loc[2] = -45 #150 #120
		elif self.legNr == 4 :
			loc[0] = 45 
			loc[1] = 90 #40.68
			loc[2] = -45 #150 #120
		elif self.legNr == 5 :
			loc[0] = 0 
			loc[1] = 90 #40.68
			loc[2] = -45 #150 #120
		elif self.legNr == 6 :
			loc[0] = -45 
			loc[1] = 90 #40.68
			loc[2] = -45 #150 #120

		#standaard waarden override
		loc[0] = 0 #set 'em all to 512
		loc[1] = 90 #40.68
		loc[2] = -45 #150 #120
		
		self.moveSpeedRW(10*self.legNr+1, loc[0])
		self.moveSpeedRW(10*self.legNr+2, loc[1])
		self.moveSpeedRW(10*self.legNr+3, loc[2])
		ax.action() # TODO do this here?
		
	#part 1b: van achter naar midden, door de lucht.
	def stepOne(self, size):
		loc = [0,0]
		if self.legNr == 1 : 
			loc[0] = 45 / size
		elif self.legNr == 3 :
			loc[0] = 9.73 / size
		elif self.legNr == 5 :
			loc[0] = -30 / size
			
		elif self.legNr == 2 :
			loc[0] = -45 / size
		elif self.legNr == 4 :
			loc[0] = -9.73 / size
		elif self.legNr == 6 :
			loc[0] = 30 / size
		loc[1] = -5	#-10
		
		self.moveSpeedRW(10*self.legNr+1, loc[0])
		self.moveSpeedRW(10*self.legNr+2, loc[1]) 

	#part 1b: van midden naar voor, door de lucht.
	def stepTwo(self, size) :
		loc = [0,0]
		if self.legNr == 1 : 
			loc[0] = 9.73 / size
		elif self.legNr == 3 :
			loc[0] = 45 / size
		elif self.legNr == 5 :
			loc[0] = -30 / size
		elif self.legNr == 2 :
			loc[0] = -9.73 / size
		elif self.legNr == 4 :
			loc[0] = -45 / size
		elif self.legNr == 6 :
			loc[0] = 30 / size
		loc[1] = 5 #10
	
		self.moveSpeedRW(10*self.legNr+1, loc[0])
		self.moveSpeedRW(10*self.legNr+2, loc[1]) 

	#part 2a: van voor naar het midden, over de grond
	def stepThree(self) :	
		loc = [0,0,0]
		if self.legNr == 1 : 		
			loc[0] = -9.73
			loc[1] = 42.37
			loc[2] = 137.17
		elif self.legNr == 3 :
			loc[0] = -45
			loc[1] = 42.37
			loc[2] = 137.17
		elif self.legNr == 5 :
			loc[0] = 30
			loc[1] = 40.68 - 1.81
			loc[2] = 120 + 8.49
			
		elif self.legNr == 2 :
			loc[0] = -30
			loc[1] = 40.68 - 1.81
			loc[2] = 120 + 8.49
		elif self.legNr == 4 :
			loc[0] = 45
			loc[1] = 42.37
			loc[2] = 137.17
		elif self.legNr == 6 :
			loc[0] = 9.73
			loc[1] = 42.37
			loc[2] = 137.17
		
		self.moveSpeedRW(10*self.legNr+1, loc[0])
		self.moveSpeedRW(10*self.legNr+2, loc[1]) 
		self.moveSpeedRW(10*self.legNr+3, loc[2]) 	
	
	#part 2b: van het midden naar achteren, over de grond.
	def stepFour(self) :
		loc = [0,0,0]
		if self.legNr == 1 : 		
			loc[0] = -45
			loc[1] = -34.86
			loc[2] = -103.62
		elif self.legNr == 3 :
			loc[0] = -9.73
			loc[1] = -34.86
			loc[2] = -103.62
		elif self.legNr == 5 :
			loc[0] = 30
			loc[1] = 40.68 + 1.81
			loc[2] = 120 - 8.49	
		elif self.legNr == 2 :
			loc[0] = -30
			loc[1] = 40.68 + 1.81
			loc[2] = 120 - 8.49
		elif self.legNr == 4 :
			loc[0] = 9.73
			loc[1] = -34.86
			loc[2] = -103.62 
		elif self.legNr == 6 :
			loc[0] = 45
			loc[1] = -34.86
			loc[2] = -103.62
		self.moveSpeedRW(10*self.legNr+1, loc[0])
		self.moveSpeedRW(10*self.legNr+2, loc[1]) 
		self.moveSpeedRW(10*self.legNr+3, loc[2]) 
	
def walking(steps) :
#method for all six legs, to walk.
	if len(feet) < 6 :
		print "ERROR! Not enough legs connected to walk!"
	else :
		if debug : print "Going a little cube around :P" #een blokje om gaan :P
#		for leg in feet: leg.ready()
#		ax.action()
#		sleep(0.1)
#		for leg in feet: leg.set()
#		ax.action()
#		sleep(0.1)
#		for leg in feet: leg.go()
#		ax.action()
#		sleep(1.0)
		
		while steps :
			for leg in feet:
				if(leg.legNr%2 == 0) : leg.stepFour()
				else : leg.stepTwo(2)
			ax.action()
			sleep(0.1)
			
			for leg in feet:
				if(leg.legNr%2 == 0) : leg.stepOne(2)
				else : leg.stepThree()
			ax.action()
			sleep(0.5)
			
			for leg in feet:
				if(leg.legNr%2 == 0) : leg.stepTwo(2)
				else : leg.stepFour()
			ax.action()
			sleep(0.1)
			
			for leg in feet:
				if(leg.legNr%2 == 0) : leg.stepThree()
				else : leg.stepOne(2)
			ax.action()
			sleep(0.5)
			
			steps = steps - 1

#main function
try :
	list = ax.learnServos(10,64)
	only = ""
	for i in range(1,7) :
		if 10*i+1 in list and 10*i+2 in list and 10*i+3 in list :
			feet.append(Foot(i))
		else :
			if 10*i+1 not in list and 10*i+2 not in list and 10*i+3 not in list :
				if debug: print "Error! Not a single servo from leg " + str(i) + " is attached!"
			else :
				if debug: print "Error! Not all servo's from leg " + str(i) + " are attached!"
			only = "Only "
	print only + str(len(feet)) + " legs initialized. Now to conquer the world."
	
#	for leg in feet: 
#		leg.go()
#		leg.rest()
#	ax.action()

	steps = 10
#	steps = input("How many steps?")
	
	sleep(0.4)
	walking(steps)
	for leg in feet:
		leg.rest()
	ax.action()
	
except KeyboardInterrupt :
	for leg in feet :
		leg.rest()
	ax.action()
	print " Exit."
