#!/usr/bin/python
import bluetooth
import json
from time import sleep
import random
import Gyro
import Joy
import threading

'''Custom exception when the server is not found'''
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
        self.move = False

    def __del__(self):
        self.shutdown()

    '''Closes the connection with the server'''
    def shutdown(self):
        print "disconnecting..."
        self.sock.close()

    '''Connects with the server, if not found raises ServerDown
       error.
    '''
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
        try:
            self.sock.send(str(json.dumps(data, separators=(',',':'))))
        except Exception, e:
            print "error sending data: ",e

    '''Starts the communication with the server'''
    def start(self):
        try:
            self.startBluetooth()
        except ServerDown as e:
            raise e

    def getBatteryStatus(self):
        get_battery_json = { "cmd" : "batteryStatus" }
        self.sendData(get_battery_json)
        try:
            battery_json = json.loads(self.readData())
            if 'cmd' in battery_json:
                cmd = battery_json['cmd']
                if cmd == 'setBattery':
                    return battery_json['battery_status']
        except Exception, e:
            print "error in read battery status: ", e
            raise e

    def moveSpid(self):
        print "in move function..."
        self.move = True
        while self.move:
            print "moving json....."
            joy_pos = [Joy.read_x(),Joy.read_y()] #TODO
            move_json = {
                    "mode" : 1,
                    "joy_pos" : joy_pos
            }
            self.sendData(move_json)
            sleep(0.05)

    def dance(self,dance_id):
        dance_json = {
                "mode" : 2,
                "danceId" : dance_id
        }
        self.sendData(dance_json)

    def attackMode(self):
        attack_json = {
            "mode" : 3
        }
        self.sendData(attack_json)

    def stab(self):
        stab_json = {
            "cmd": "stab"
        }
        self.sendData(stab_json)

    '''Sends the gyroscope position to the server.'''
    def setGyro(self,gyro_pos):
        print "gyro does work tough"
        sync_json = {
            "cmd" : "setGyro",
            "gyro" : gyro_pos
        }
        self.sendData(sync_json)

    '''Keeps the spider legs synchronized with the gyroscope position
       from the smartcontroller.
    '''
    def synchronizeFrontLegs(self):
        self.synclegs = True
        while self.synclegs:
            #get the gyro value
            #gyropositions = [Gyro.x_gyroscoop(),Gyro.y_gyroscoop(),0]
            #randomx = random.randint(-60,60)
            gyropositions = [Gyro.x_gyroscope(),Gyro.y_gyroscope(),0]
            self.setGyro(gyropositions)
            sleep(0.05)

    '''Let's the spider follow a line on the ground.'''
    def autonomousLine(self):
        line_json = { "mode" : 4 }
        self.sendData(line_json)

    '''Makes the spider walk to a balloon and pop it.'''
    def autonomousBalloon(self):
        balloon_json = { "mode" : 5 }
        self.sendData(balloon_json)

    '''Makes the spider go into sleep/carry mode'''
    def goToSleep(self):
        sleep_json = { "mode" : 6 }
        self.sendData(sleep_json)

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
    moveTest = spiderCommunication.attackMode()
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
