#!/usr/bin/python
from ax import Ax12
from time import sleep
import time
import os
import draagmodus

ax = Ax12()

a = 512.0/60.0
z = 35.0/60.0
omrek = a*z
##operates the shoulder servo, the x1 servo's
#@param id int representing the id of the servo
#@param loc int representing the location of the servo ranging from 0 to 1023
#@param speed int representing the speed of the servo ranging from 0 to 512 (1023 is possible, but won't increase the speed further)
def shoulder(id,loc,speed):  #,delay
	ax.moveSpeedRW(id,loc,speed)
	ax.action()
	sleep(0.04)
	
##operates the elbow servo, the x2 servo's
#@param id int representing the id of the servo
#@param loc int representing the location of the servo ranging from 0 to 1023
#@param speed int representing the speed of the servo ranging from 0 to 512 (1023 is possible, but won't increase the speed further)
def elbow(id,loc,speed): #,delay
	ax.moveSpeedRW(id,loc,speed)
	ax.action()
	sleep(0.04)

##operates the wrist servo, the x3 servo's
#@param id int representing the id of the servo
#@param loc int representing the location of the servo ranging from 0 to 1023
#@param speed int representing the speed of the servo ranging from 0 to 512 (1023 is possible, but won't increase the speed further)	
def wrist(id,loc,speed):
	ax.moveSpeedRW(id,loc,speed)
	ax.action()
	sleep(0.04)
	
##operates the above methods(kind of hardcoded, will be fixed in the future)
def setLegs():
	shoulder(11,674,350)
	shoulder(21,574,350)
	shoulder(31,350,350)
	shoulder(41,674,350)
	shoulder(51,450,350)
	shoulder(61,350,350)
	elbow(12,512,350)
	elbow(22,600,350)
	elbow(32,774,350)
	elbow(42,774,350)
	elbow(52,600,350)
	elbow(62,512,350)
	wrist(13,512,350)
	wrist(23,900,350)
	wrist(33,1000,350)
	wrist(43,1000,350)
	wrist(53,900,350)
	wrist(63,512,350)

##operates the stab mechanism, hardcoded as well(will be fixed in the future)
def prepareStab():
	shoulder(61,350,350)
	shoulder(11,674,350)
	elbow(12,512,350)
	elbow(62,512,350)
	wrist(13,512,350)
	wrist(63,512,350)
	

#initializing stuff for testing purposes
draagmodus.carry()
prepareStab()
setLegs()
sleep(3)
stab(0)
#while True:
#	stab(60)


