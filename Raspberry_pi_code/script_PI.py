#!/usr/bin/python
import serial
ser=serial.Serial('/dev/ttyUSB0', 9600)
while 1 :
    next=raw_input("voer een getal in: ")
    put=str(next)
    ser.write(put)
    ser.flush()
    print ser.readline()
    ser.flush()

