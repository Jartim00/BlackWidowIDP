#!/usr/bin/python
from ax import Ax12
from time import sleep
import os
ax = Ax12()


list = ax.learnServos(10, 70, False)
print list

#for(servo in list) :
#	print "id " . servo