#!/usr/bin/python
from ax import Ax12
from time import sleep
import os

ax = Ax12()
debug = True
debug2 = False
feet = []

class Foot :
	#has three servo's based on the leg number.
	legNr = 0
	
	def __init__(self, legNr) :
		self.legNr = legNr
		self.lights(True)
		
	def __repr__(self) : #self print function
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
		if debug2: print "Converting " + str(deg) + " degrees to " + str(step) + " steps." 
		if step < 0 : return 0
		elif step > 1023 : return 1023
		else : return int(step)
	
	def time(self, id, loc) :
		cur = ax.readPosition(id)
		dx = int(abs(loc - cur)) #get the distance to move
		if debug2: print "Calculating step time from " + str(cur) + " to " + str(loc) + " is " + str(dx)
		if dx < 0 : return 0
		elif dx > 1023 : return 1023
		else : return dx #int(1024 * (dx/180)) # TODO : tijd goed?
	
	def moveSpeedRW(self, id, loc) :
		loc = self.step(id, loc) #check if valid location
		spd = self.time(id, loc) #make valid time 

		ax.moveSpeedRW(id, loc, spd) 
		if debug : print "Servo: " + str(id) + " to loc: " + str(loc) + " at spd: " + str(spd)
		sleep(0.05)

	def rest(self) :
		loc = [0,0,0]
		if self.legNr == 1 :
			loc[1] = 42.37
			loc[2] = 137.17
		elif self.legNr == 2 :
			loc[1] = 40.68
			loc[2] = 120
		elif self.legNr == 3 : 
			loc[1] = 42.37
			loc[2] = 137.17
		elif self.legNr == 4 :
			loc[1] = 34.86
			loc[2] = 137.17
		elif self.legNr == 5 :
			loc[1] = 40.68 - 1.81
			loc[2] = 120 + 8.49
		elif self.legNr == 6 :
			loc[1] = 34.86
			loc[2] = 137.17
		
		#ready positions
		self.moveSpeedRW(10*self.legNr+1, loc[0])
		self.moveSpeedRW(10*self.legNr+2, loc[1])
		self.moveSpeedRW(10*self.legNr+3, loc[2])
		
	#part 1b: van achter naar midden, door de lucht.
	def stepOne(self):
		loc = [0,0]
		if self.legNr == 1 : 
			loc[0] = 0
		elif self.legNr == 3 :
			loc[0] = 0
		elif self.legNr == 5 :
			loc[0] = 0
		elif self.legNr == 2 :
			loc[0] = 0
		elif self.legNr == 4 :
			loc[0] = 0
		elif self.legNr == 6 :
			loc[0] = 0
		loc[1] = 40.68 + 5
		
		self.moveSpeedRW(10*self.legNr+1, loc[0])
		self.moveSpeedRW(10*self.legNr+2, loc[1]) 

	#part 1b: van midden naar voor, door de lucht.
	def stepTwo(self) :
		loc = [0,0,0]
		if self.legNr == 1 : 
			loc[0] = 9.73
			loc[1] = 34.86
			loc[2] = 103.62
		elif self.legNr == 3 :
			loc[0] = 45 
			loc[1] = 34.86
			loc[2] = 103.62
		elif self.legNr == 5 :
			loc[0] = -30
			loc[1] = 31.38
			loc[2] = 95.56
		elif self.legNr == 2 :
			loc[0] = -30
			loc[1] = 31.38
			loc[2] = 95.56
		elif self.legNr == 4 :
			loc[0] = 9.73 
			loc[1] = 34.86
			loc[2] = 103.62
		elif self.legNr == 6 :
			loc[0] = 45
			loc[1] = 34.86
			loc[2] = 103.62
		#loc[1] = 40.68 + 5 #10 # TODO
	
		self.moveSpeedRW(10*self.legNr+1, loc[0])
		self.moveSpeedRW(10*self.legNr+2, loc[1]) 
		self.moveSpeedRW(10*self.legNr+3, loc[2]) 

	#part 2a: van voor naar het midden, over de grond
	def stepThree(self) :	
		loc = [0,0,0]
		if self.legNr == 1 : 		
			loc[0] = 0
			loc[1] = 42.37-5
			loc[2] = 137.17
		elif self.legNr == 2 :
			loc[0] = 0
			loc[1] = 40.68 - 1.81 -5 
			loc[2] = 120 + 8.49
		elif self.legNr == 3 :
			loc[0] = 0
			loc[1] = 42.37-5
			loc[2] = 137.17
		elif self.legNr == 4 :
			loc[0] = 0
			loc[1] = 42.37-5
			loc[2] = 137.17
		elif self.legNr == 5 :
			loc[0] = 0
			loc[1] = 40.68 - 1.81-5
			loc[2] = 120 + 8.49
		elif self.legNr == 6 :
			loc[0] = 0
			loc[1] = 42.37-5
			loc[2] = 137.17
		
		#self.moveSpeedRW(10*self.legNr+2, loc[1]) # TODO
		#self.moveSpeedRW(10*self.legNr+3, loc[2]) # TODO	
		self.moveSpeedRW(10*self.legNr+1, loc[0])	
	
	#part 2b: van het midden naar achteren, over de grond.
	def stepFour(self) :
		loc = [0,0,0]
		if self.legNr == 1 : 		
			loc[0] = -45
			loc[1] = 34.86
			loc[2] = 103.62
		elif self.legNr == 2 :
			loc[0] = 30
			loc[1] = 40.68 + 1.81
			loc[2] = 120 - 8.49
		elif self.legNr == 3 :
			loc[0] = -9.73
			loc[1] = 34.86
			loc[2] = 103.62
		elif self.legNr == 4 :
			loc[0] = -45
			loc[1] = 34.86
			loc[2] = 103.62 
		elif self.legNr == 5 :
			loc[0] = 30
			loc[1] = 40.68 + 1.81
			loc[2] = 120 - 8.49	
		elif self.legNr == 6 :
			loc[0] = -9.73
			loc[1] = 34.86
			loc[2] = 103.62
			
		self.moveSpeedRW(10*self.legNr+1, loc[0])
		self.moveSpeedRW(10*self.legNr+2, loc[1]) 
		self.moveSpeedRW(10*self.legNr+3, loc[2]) 
	
def walking(steps) :
#method for all six legs, to walk.
	if len(feet) < 6 :
		print "ERROR! Not enough legs connected to walk!"
	else :
		if debug : print "Going a little cube around :P" #een blokje om gaan :P
		
		delay = 0.2
		while steps :
			for leg in feet:
				leg.stepFour()
			ax.action()
			sleep(delay)
			
			for leg in feet:
				leg.stepOne()
			ax.action()
			sleep(delay)
			
			for leg in feet:
				leg.stepTwo()
			ax.action()
			sleep(delay)
			
			for leg in feet:
				leg.stepThree()
			ax.action()
			sleep(delay)
			
			steps = steps - 1

#main function
try :
	list = ax.learnServos(10,64)
	only = ""
	exit = False
	for i in range(1,7) :
		if 10*i+1 in list and 10*i+2 in list and 10*i+3 in list :
			feet.append(Foot(i))
			if debug: print "Added foot " + str(i) + " to the list."
		else :
			if 10*i+1 not in list and 10*i+2 not in list and 10*i+3 not in list :
				if debug: print "Error! Not a single servo from leg " + str(i) + " is attached!"
			else :
				if debug: print "Error! Not all servo's from leg " + str(i) + " are attached!"
			only = "Only "
			exit = True
	print only + str(len(feet)) + " legs initialized. Now to conquer the world."
#	if exit == True : exit() #if less than 6 legs, kill the program. # TODO
		
	for leg in feet: 
		leg.rest()
	ax.action()
	#voeten klaarzetten

	steps = 10
#	steps = input("How many steps?")
	
	sleep(0.4)
	walking(steps)
	for leg in feet:
		leg.rest()
		ax.action() # TODO one leg at a time or all at once? (2 tabs or one?)
	
except KeyboardInterrupt :
	for leg in feet :
		leg.rest()
		leg.lights(False)
	ax.action()
	print " Exit."
