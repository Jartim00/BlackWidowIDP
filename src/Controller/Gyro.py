#!/usr/bin/python
import smbus
import math
import time

# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

def accel_xout_scaled():
    return read_word_2c(0x3b) / 16384.0

def accel_yout_scaled():
    return read_word_2c(0x3d) / 16384.0

def accel_zout_scaled():
    return read_word_2c(0x3f) / 16384.0

def x_gyroscoop():
    if get_x_rotation(accel_xout_scaled(), accel_yout_scaled(), accel_zout_scaled()) <= -60:
        return -60
    if get_x_rotation(accel_xout_scaled(), accel_yout_scaled(), accel_zout_scaled()) >= 60:
        return 60
    else:
        return (int)(get_x_rotation(accel_xout_scaled(), accel_yout_scaled(), accel_zout_scaled()))

def y_gyroscoop():
    return (int)(get_y_rotation(accel_xout_scaled(), accel_yout_scaled(), accel_zout_scaled()))

def z_gyroscoop():
    pass
 	
bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
address = 0x68       # This is the address value read via the i2cdetect command


# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)
