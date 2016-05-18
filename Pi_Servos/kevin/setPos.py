#!/usr/bin/python
from ax import Ax12
from time import sleep
import os

ax = Ax12()
leg = 2

ax.move(leg*10+1, 512)
sleep(0.1)
ax.move(leg*10+2, 512)
sleep(0.1)
ax.move(leg*10+3, 512)
sleep(0.1)

#1023 eenheden
#1 eenheid is 0.289648438
