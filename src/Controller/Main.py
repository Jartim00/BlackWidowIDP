#!/usr/bin/python
import time
import ADC
import Gyro
import os
import Screen

# X waarde in graden (-60/60): Gyro.get_x_rotation(Gyro.accel_xout_scaled(), Gyro.accel_yout_scaled(), Gyro.accel_zout_scaled())
# y waarde in graden (-60/60): Gyro.get_y_rotation(Gyro.accel_xout_scaled(), Gyro.accel_yout_scaled(), Gyro.accel_zout_scaled())

# x waarde joy (-60/60): ADC.joy_x()
# y waarde joy (-60/60): ADC.joy_y()

def Joy_x():
        return ADC.joy_x()

def Joy_y():
        return ADC.joy_y()

def Gyro_x():
        return Gyro.get_x_rotation(Gyro.accel_xout_scaled(), Gyro.accel_yout_scaled(), Gyro.accel_zout_scaled())

def Gyro_y():
        return Gyro.get_y_rotation(Gyro.accel_xout_scaled(), Gyro.accel_yout_scaled(), Gyro.accel_zout_scaled())

Screen.active_background()
Screen.mode_1()
Screen.main_loop()

while 1:
        print "werkt"
        time.sleep(0.01)

# print " gyro x waarde",Gyro.x_gyroscoop()
 #   print " gyro y waarde",Gyro.y_gyroscoop()
  #  print "\n joy x waarde",ADC.joy_x()
  #  print " joy y waarde",ADC.joy_y()
  #  time.sleep(0.5)
#    os.system('clear')
