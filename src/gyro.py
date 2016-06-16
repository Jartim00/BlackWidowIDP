#!/usr/bin/python
import smbus
import math
import time

# Power management registers.
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

## Reads a raw byte from the selected I2C chip.
# @param adr the I2C address of the chip
def read_byte(adr):
    return bus.read_byte_data(address, adr)

## Reads a raw word from the selected I2C chip.
# @param adr the I2C address of the chip
def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

## Converts two's complement to an int value.
# @param adr the I2C address of the chip
def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

## Uses the Pythagorean theorem on two values.
# @param a,b accelerometer values
def dist(a,b):
    return math.sqrt((a*a)+(b*b))

## Calculates the y rotation angle from the gravity that is exerting on the sensor.
# @param x,y,z raw data from the accelerometer
def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

## Calculates the x rotation angle from the gravity that is exerting on the sensor.
# @param x,y,z raw data from the accelerometer
def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

## Scales the gravity value.
def accel_xout_scaled():
    return read_word_2c(0x3b) / 16384.0

## Scales the gravity value.
def accel_yout_scaled():
    return read_word_2c(0x3d) / 16384.0

## Scales the gravity value.
def accel_zout_scaled():
    return read_word_2c(0x3f) / 16384.0

## Limits the output values to 60 and -60 and converts the angles to int instead of float.
def x_gyroscope():
    if get_x_rotation(accel_xout_scaled(), accel_yout_scaled(), accel_zout_scaled()) <= -60:
        return -60
    if get_x_rotation(accel_xout_scaled(), accel_yout_scaled(), accel_zout_scaled()) >= 60:
        return 60
    else:
        return (int)(get_x_rotation(accel_xout_scaled(), accel_yout_scaled(), accel_zout_scaled()))

## Converts the angles to int instead of float.
def y_gyroscope():
    return (int)(get_y_rotation(accel_xout_scaled(), accel_yout_scaled(), accel_zout_scaled()))

## Does nothing.
def z_gyroscope():
    pass

bus = smbus.SMBus(1)
address = 0x69


## Wakes the chip as it starts in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)

## Loop to test the gyro
'''while True:
    print "x value:"
    print x_gyroscope()
    print "y value:"
    print y_gyroscope()
    time.sleep(0.5)
'''
