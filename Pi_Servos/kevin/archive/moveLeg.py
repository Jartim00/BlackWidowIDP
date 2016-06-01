#!/usr/bin/python
from ax import Ax12
from time import sleep
from multiprocessing import Process
from readValues import readValues, prN, speed
import os

#define HEUP 10*leg+1
#define KNIE 10*leg+2
#define VOET 10*leg+3
#HOE MOET DIT IN PYTHON?
#DEFINE is namelijk C-synt

ax = Ax12()
leg = 2
_HEUP = 10*leg+1
_KNIE = 10*leg+2
_VOET = 10*leg+3
_FACTOR = 0.29296875 #300/1024 -> omrekenfactor van graden naar stappen
_DELAY = 0.5

debug = True

def moveSpeed(id, loc, spd) : #move with a given speed
	ax.moveSpeed(id, loc, spd)

def move(id, loc, spd=512) :
	if(debug) : print id, " to ", loc
	if(loc >= 0 and loc <= 1023) :
		ax.move(id, int(loc)) #cast float loc to int
		sleep(_DELAY)
	elif (loc > 1023) :
		ax.move(id, 1023)
		sleep(_DELAY)
	elif (loc < 0) :
		ax.move(id, 0)
		sleep(_DELAY)
	else :
		print "ERROR: loc (", loc, ") == BORKED!"
	
def moveTogether(ida, loca, idb, locb, idc, locc) :
	#placeholder functie voor tegelijk bewegen van servo's
	move(ida, loca)
	move(idb, locb)
	move(idc, locc)

def lights(leg, status) :
	#zet alle lampjes aan
	ax.setLedStatus(_HEUP, status)
	ax.setLedStatus(_KNIE, status)
	ax.setLedStatus(_VOET, status)
	
def goToStartPos(leg) :
	if(debug) : print "Start position!"
	#breng terug naar beginstand
	move(_KNIE,810)
	move(_VOET,820)
	
	#uiteindelijke beginstand
	move(_HEUP, 512) #recht opzij
	move(_VOET, 512+(150/_FACTOR)) # 1023
	#VOET dode hoek naar bovenkant? -> dan 1023 - (90/_FACTOR)
	move(_KNIE, 512+(75/_FACTOR)) # 768

def walk(leg) :
	#part 1: van achter naar voren, door de lucht
	if(debug) : print "Hey ho,"
	move(_KNIE, 650) #650
	move(_VOET, 900) #900
	move(_HEUP, 512-(30/_FACTOR)) #615.44
	
	#part 2a: van voor naar het midden, over de grond
	if(debug) : print "hey ho, "
	moveTogether(
		_HEUP, 512, #naar t midden
		_KNIE, 719, #719
		_VOET, 983, #983
		)
	
	#part 2b: van het midden naar achteren, over de grond.
	#eigenlijk inverse part 2a.
	if(debug) : print "je krijgt me niet cadeau"
	moveTogether( 
	_HEUP, 512+(30/_FACTOR), #408.55
	_KNIE, 512+(75/_FACTOR), #beginstand
	_VOET, 512+(150/_FACTOR), #beginstand
	)
	
def walkdemo(leg) :
	#demo walk
	ax.move(_KNIE,810)
	ax.move(_VOET,512)
	ax.move(_HEUP,350)
	ax.move(_VOET,210)
	ax.move(_KNIE,610)
	ax.move(_HEUP,670)

def moveLeg(leg) :
	lights(leg, True)
	goToStartPos(leg)
	while(True):
		walkdemo(leg)
#		walk(leg)

p1 = Process(target=readValues)
try:
	leg = input('Leg nr (1-6):')
	moveLeg(leg)
	p1.start()

except KeyboardInterrupt :
	screenRunning = False
	goToStartPos(leg)
	lights(leg, False)
