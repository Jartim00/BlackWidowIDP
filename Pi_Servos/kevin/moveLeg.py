#!/usr/bin/python
from ax import Ax12
from time import sleep
from multiprocessing import Process
import os

#define HEUP 10*leg+1
#define KNIE 10*leg+2
#define VOET 10*leg+3
#HOE MOET DIT IN PYTHON?
#DEFINE is namelijk C-syntax.

ax = Ax12()
leg = 2
_HEUP = 10*leg+1
_KNIE = 10*leg+2
_VOET = 10*leg+3
_FACT = 0.29296875 #300/1024 -> omrekenfactor van graden naar stappen

def move(id, loc) :
	ax.move(id, loc)
	sleep(0.5)
	
def moveTogether(ida, loca, idb, locb, idc, locc) :
	#placeholder functie voor tegelijk bewegen van servo's
	move(ida, loca)
	move(idb, locb)
	move(idc, locc)
	
def getLeg():
	leg = 2 #ask input
	_HEUP = 10*leg+1
	_KNIE = 10*leg+2
	_VOET = 10*leg+3
	return leg

def lights(leg, status) :
	#zet alle lampjes aan
	ax.setLedStatus(_HEUP, status)
	ax.setLedStatus(_KNIE, status)
	ax.setLedStatus(_VOET, status)
	
def goToStartPos(leg) :
	#breng terug naar beginstand
	move(_KNIE,810)
	move(_VOET,820)
	
	#uiteindelijke beginstand
	move(_HEUP,512) #recht opzij
	move(_VOET,725) #512-(180/_FACT) = 
	move(_KNIE,715) #512+(90/_FACT) = 201.66

def walk(leg) :
	#part 1: van achter naar voren, door de lucht
	move(_KNIE, )
	move(_VOET, ) 
	move(_HEUP, 512-(30/_FACT)) #615.44
	
	#part 2a: van voor naar het midden, over de grond
	moveTogether(
		_HEUP, 512,
		_KNIE, ,
		_VOET, ,
		)
	
	#part 2b: van het midden naar achteren, over de grond.
	#eigenlijk inverse part 2a.
	moveTogether(
	_HEUP, 512+(30/_FACT), #408.55
	_KNIE, ,
	_VOET, ,
	)
	
def walkdemo(leg) :
	#demo walk
	move(_KNIE,810)
	move(_VOET,820)
	move(_HEUP,350)
	move(_VOET,512)
	move(_KNIE,610)
	move(_HEUP,670)

def moveLeg(leg) :
	lights(leg, True)
	goToStartPos(leg)
	while(True):
		walkdemo(leg)

try:
	leg = getLeg()
	moveLeg(leg)
except KeyboardInterrupt:
	goToStartPos(leg)
	lights(leg, False)
	
