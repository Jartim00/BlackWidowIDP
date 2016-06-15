import Adafruit_ADS1x15
import time
adc = Adafruit_ADS1x15.ADS1015()
waarde1=2000
waarde2=2000
waarde3=2000
waarde4=2000
waarde5=2000
leeg=2000
gem_sample=0
def gem5():
    global waarde1
    global waarde2
    global waarde3
    global waarde4
    global waarde5
    global leeg
    waarde5=waarde4
    waarde4=waarde3
    waarde3=waarde2
    waarde2=waarde1
    waarde1=adc.read_adc(2,gain=2/3)
    if(waarde1>1200):
        if(waarde5==leeg):
            if(waarde4==leeg):
                if(waarde3==leeg):
                    if(waarde2==leeg):
                        return waarde1
                    else:
                        return (waarde1+waarde2)/2
                else:
                    return (waarde1+waarde2+waarde3)/3
            else:
                return (waarde1+waarde2+waarde3+waarde4)/4
        else:
            return (waarde1+waarde2+waarde3+waarde4+waarde5)/5
    else:
        return 1200
def read():
    global gem_sample
    gem_sample=gem5()
    global waarde1
    if(waarde1<1200):
        return 0
    if(gem_sample>1600):
        return 4
    if(gem_sample>1500):
        return 3
    if(gem_sample>=1400):
        return 2
    if(gem_sample<1400):
        return 1


'''    
while True:
    print read()
    time.sleep(0.5)
'''
