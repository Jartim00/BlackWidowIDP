#!/usr/bin/python
import bluetooth
import json
from time import sleep
import random
#import Gyro
import Joy

class ServerDown(Exception):

    def __init__(self,value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class SpiderCommunication(object):

    def __init__(self,bd_addr,port):
        self.bd_addr = bd_addr
        self.port = port
        self.synclegs = False

    def __del__(self):
        self.shutdown()

    def shutdown(self):
        print "disconnecting..."
        self.sock.close()

    def startBluetooth(self):
        # devices = bluetooth.discover_devices()
        # if self.bd_addr not in devices:
        #     raise ServerDown("Couldn't find the server")
        try:
            self.sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
            self.sock.connect((self.bd_addr,self.port))
        except bluetooth.btcommon.BluetoothError:
			raise ServerDown("Couldn't find the server")

    def readData(self):
        return self.sock.recv(1024)

    def sendData(self,data):
        self.sock.send(str(json.dumps(data, separators=(',',':'))))

    def start(self):
        try:
            self.startBluetooth()
        except ServerDown as e:
            raise e

    def getBatteryStatus(self):
        battery_json = { "cmd" : "batteryStatus" }
        self.sendData(battery_json)
        return self.readData()

    def move(self,joy_x,joy_y):
        move_json = {
                "mode" : 1,
                "joy_x" : joy_x,
                "joy_y" : joy_y
            }
        self.sendData(move_json)
        return self.readData()

    def dance(self,dance_id):
        dance_json = {
                "mode" : 2,
                "danceId" : dance_id
        }
        self.sendData(dance_json)
        return self.readData()

    def stab(self):
        stab_json = {
            "mode" : 3
        }
        self.sendData(stab_json)
        return self.readData()

    def setGyro(self,gyro_pos):
        sync_json = {
            "cmd" : "setGyro",
            "gyro" : gyro_pos
        }
        self.sendData(sync_json)
        return self.readData()

    def synchronizeFrontLegs(self):
        self.synclegs = True
        while self.synclegs:
            #get the gyro value
            #gyropositions = [Gyro.x_gyroscoop(),Gyro.y_gyroscoop(),0]
            #randomx = random.randint(-60,60)
            gyropositions = [Joy.read_x(),Joy.read_y(),0]
            self.setGyro(gyropositions)
            sleep(0.05)

    def autonomousLine(self):
        line_json = { "mode" : 4 }
        self.sendData(line_json)
        return self.readData()

    def autonomousBalloon(self):
        balloon_json = { "mode" : 5 }
        self.sendData(balloon_json)
        return self.readData()

    def goToSleep(self):
        sleep_json = { "mode" : 6 }
        self.sendData(sleep_json)
        return self.readData()

def main():
    spiderCommunication = SpiderCommunication("00:1A:7D:DA:71:06",1)
    try:
        spiderCommunication.start()
    except ServerDown as e:
        print e.value
        return -1
    moveTest = spiderCommunication.move(22.35,55.23)
    print moveTest
    moveTest = spiderCommunication.getBatteryStatus()
    print moveTest
    moveTest = spiderCommunication.dance(2)
    print moveTest
    moveTest = spiderCommunication.stab()
    print moveTest
    moveTest = spiderCommunication.synchronizeFrontLegs(56)
    print moveTest
    moveTest = spiderCommunication.autonomousLine()
    print moveTest
    moveTest = spiderCommunication.autonomousBalloon()
    print moveTest
    moveTest = spiderCommunication.goToSleep()
    print moveTest


if __name__ == "__main__":
    main()
