#!/usr/bin/python
import math
from ax import Ax12
from time import sleep
from kinematic import Kinematic
import os
ax = Ax12()
bx = Kinematic()

##Puts the hexapod in carry mode
#@param leg int representing a number between 1 and 6. For instance:1 inside the first try makes it so that all servos ranging from 11 to 13 move
def rest(self, leg) :
        offset = 71
        loc = [0,0]
        if leg == 1 :
            loc = bx.calc_angles(0, 84.24478972, offset)
        elif leg == 2 :
            loc = bx.calc_angles(0, 103.1783, offset)
        elif leg == 3 :
            loc = bx.calc_angles(0, 84.24478972, offset)
        elif leg == 4 :
            loc = bx.calc_angles(0, 84.24478972, offset)
        elif leg == 5 :
            loc = bx.calc_angles(0, 103.1783, offset)
        elif leg == 6 :
            loc = bx.calc_angles(0, 84.24478972, offset)
        #ready positions
        try:
            ax.moveSpeedRW(leg*10 + 1, 512, 450)
            ax.moveSpeedRW(leg*10 + 2, loc[0], 450)
            ax.moveSpeedRW(leg*10 + 3, loc[1], 450)
            sleep(0.04)
        except:
            try:
                ax.moveSpeedRW(leg*10 + 1, 512, 450)
                ax.moveSpeedRW(leg*10 + 2, loc[0], 450)
                ax.moveSpeedRW(leg*10 + 3, loc[1], 450)
                sleep(0.04)
            except:
    	       pass
