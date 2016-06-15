import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1015()

def read_y():
    return ((adc.read_adc(0,gain=1)+5)/10)-122

def read_x():
    return ((adc.read_adc(1,gain=1)+5)/10)-122

#while True:
#    waarde = adc.read_adc(i,gain=GAIN)
#    print waarde
#    time.sleep(0.5)
