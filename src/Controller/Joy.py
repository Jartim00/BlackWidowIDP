#!/usr/bin/python
import time
import Adafruit_ADS1x15
waarde1=0;
waarde2=0;
adc = Adafruit_ADS1x15.ADS1015()

def read_y():
    return ((adc.read_adc(0,gain=1)+5)/10)-122
    #return adc.read_adc(0,gain=1);

def read_x():
    return ((adc.read_adc(1,gain=1)+5)/10)-122
    #return adc.read_adc(1,gain=1);

'''while True:
    waarde1=read_y();
    waarde2=read_x();
    print "joy y: "
    print waarde1
    print "joy x: "
    print waarde2
    time.sleep(0.5)'''
