#!/usr/bin/python
import math
from ax import Ax12
from time import sleep
from kinematic import Kinematic
import os
ax = Ax12()
bx = Kinematic()

class Bridge:
    isMoving = False
    ##Ready legs for Bridge
    def readyForBridge(self):
        isMoving = True
        loc = [0,0]
        for leg in range(1,7):
            loc = bx.calc_angles(0, 84.24478972, 0)
            ax.moveSpeedRW(leg*10 + 2, loc[0], 450)
            ax.moveSpeedRW(leg*10 + 3, loc[1], 450)
            if leg == 2 or leg == 5:
                ax.moveSpeedRW(leg*10 + 1, 512, 450)
            elif leg ==  1 or leg == 4:
                ax.moveSpeedRW(leg*10 + 1, bx.AngleToServo(60), 450)
            elif leg == 1 or leg == 6:
                loc = bx.calc_angles(0, 120, 0)
                ax.moveSpeedRW(leg*10 + 2, loc[0], 450)
                ax.moveSpeedRW(leg*10 + 3, loc[1], 450)                
            else:
                ax.moveSpeedRW(leg*10 + 1, bx.AngleToServo(-60), 450)
        isMoving = False
        ax.action()

    def rups(self):
        #raise from ground
        for x in range(1,7,5):
            #front legs 1 and 6
            loc = bx.calc_angles(0, 120, 30)
            ax.moveSpeedRW(x*10 + 2, loc[0], 450)
            ax.moveSpeedRW(x*10 + 3, loc[1], 450)
        for x in range(3,4):
            #rear legs 3 and 4
            loc = bx.calc_angles(0, 84.24478972, 30)
            ax.moveSpeedRW(leg*10 + 2, loc[0], 450)
            ax.moveSpeedRW(leg*10 + 3, loc[1], 450)
        ax.action()
        sleep(0.2)
        #push spider forward
        for x in range(1,7,5):
            #front legs 1 and 6
            loc = bx.calc_angles(0, 84.24478972, 30)
            ax.moveSpeedRW(leg*10 + 2, loc[0], 450)
            ax.moveSpeedRW(leg*10 + 3, loc[1], 450)
        for x in range(3,4):
            #rear legs 3 and 4
            loc = bx.calc_angles(0, 120, 30)
            ax.moveSpeedRW(x*10 + 2, loc[0], 450)
            ax.moveSpeedRW(x*10 + 3, loc[1], 450)
        ax.action()
        sleep(0.5)
        for x in range(1,7,5):
            #front legs 1 and 6
            loc = bx.calc_angles(0, 120, 0)
            ax.moveSpeedRW(x*10 + 2, loc[0], 450)
            ax.moveSpeedRW(x*10 + 3, loc[1], 450)
        for x in range(3,4):
            #rear legs 3 and 4
            loc = bx.calc_angles(0, 84.24478972, 0)
            ax.moveSpeedRW(leg*10 + 2, loc[0], 450)
            ax.moveSpeedRW(leg*10 + 3, loc[1], 450)
        ax.action()
        sleep(0.2)
        
		
