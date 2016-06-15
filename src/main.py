#!/usr/bin/python
from flask import Flask, render_template, Response, request
from camera_pi import Camera
import json
import threading
from multiprocessing import Process
from servo import Servo
from time import sleep
from ax import Ax12
#import vision.vision
import communication.btserver as btserver
import communication.appserver as appserver
import spider_battery
import gyro
ax = Ax12()

class MainProgram(object):
    servos = []
    def __init__(self):
        self.createServos(6,3)
        self.joyPos = [0,0] #x,y
        self.gyroPos = [0,0,0] #x,y,z

    ## Starts the main program
    def start(self):
        self.running = True
        self.startRESTAPI()
        self.startBluetoothServer()
        self.startAppServer()
        self.startUpdateThread()
        #continuous updates
        while self.running:
            try:
                sleep(1)
            except KeyboardInterrupt:
                print "exiting mainprogram..."
                self.shutdown()
                return

    ## Shuts down the application
    def shutdown(self):
        self.running = False
        self.bluetoothServer.stop()
        self.appServer.stop()
        #shutdown flask
        #self.apiserver.terminate()
        #self.apiserver.join()
        # self.shutdown_server()

    # def shutdown_server(self):
    #     func = request.environ.get('werkzeug.server.shutdown')
    #     if func is None:
    #         raise RuntimeError('Not running with the Werkzeug Server')
    #     func()

    ## Creates servo objects for REST API
    # @param numLegs The number of legs
    # @param servosPerLeg The number of servo's per leg
    def createServos(self,numLegs,servosPerLeg):
        if not 1 <= servosPerLeg <= 9:
            return
        self.servos = [Servo(servoId) for servoId in ax.learnServos(10,70)]
        '''for legNum in range(10,(numLegs + 1) * 10,10):
            for servoNum in range(1,servosPerLeg+1):
                #create servo
                servoId = legNum + servoNum
                self.servos.append(Servo(servoId))'''

    ## Starts all update threads
    def startUpdateThread(self):
        print "starting update thread..."
        threading.Thread(target=self.fastAPIUpdates,args=(self.servos,)).start()
        threading.Thread(target=self.slowAPIUpdates).start()

    ## Starts the REST API
    def startRESTAPI(self):
        restapi = RestAPI(self)
        self.apiserver = threading.Thread(target=restapi.start)
        self.apiserver.daemon = True
        self.apiserver.start()

    ## Starts the bluetooth server for communication with the controller
    def startBluetoothServer(self):
        self.bluetoothServer = btserver.BluetoothServer("",1,self)
        self.bluetoothThread = threading.Thread(target=self.bluetoothServer.start)
        self.bluetoothThread.daemon = True
        self.bluetoothThread.start()

    ## Starts the API server for the app
    def startAppServer(self):
        self.appServer = appserver.AppServer("",1337)
        # self.appServer.setServos(self.servos)
        self.appServerThread = threading.Thread(target=self.appServer.start)
        self.appServerThread.start()

    ## Returns the battery status from the spider.
    #  This is a value from 0 through 4
    def getBatteryStatus(self):
        return spider_battery.read()

    ## Returns the gyroscope position of the spider
    def getGyroPos(self):
        return [gyro.x_gyroscope(),gyro.y_gyroscope()]

    ## Returns the gyroscope position of the controller
    def getControllerGyroPos(self):
        return self.gyroPos

    ## Sets the gyroscope position of the controller
    def setControllerGyroPos(self,gyroPos):
        self.gyroPos = gyroPos

    ## Returns the joystick position of the controller
    def getJoyPos(self):
        return self.joyPos

    ## Sets the joystick position of the controller
    def setJoyPos(self,joyPos):
        self.joyPos = joyPos

    ## Returns a JSON string which is sent in fast API updates
    def getFastAPIJSON(self):
        infoJSON = {"servos":[],
                    "gyro":self.getGyroPos(),
                    "joy_pos":self.getJoyPos()
                    }
        for servo in self.servos:
            infoJSON["servos"].append(
            {
                "id":servo.getId(),
                "temperature": servo.getTemperature(),
                "load": servo.getLoad(),
                "voltage": servo.getVoltage(),
                "position":servo.getPosition(),
                "moving": servo.getMovingStatus()
            })
        return json.dumps(infoJSON, separators=(',',':'))

    ## Returns a JSON string which is sent in slow API updates
    def getSlowAPIJSON(self):
        infoJSON = {"spiderBattery":self.getBatteryStatus(),#TODO
                    "controllerBattery":4#TODO
                    }
        return json.dumps(infoJSON, separators=(',',':'))

    ## Updates all servo values.
    #  @param toUpdateServos An array containing the servo class objects
    def updateServos(self,toUpdateServos):
       for servo in toUpdateServos:
           try:
               servo.updateVariables()
           except ax.timeoutError:
               print "error...."

    ## Updates API info which needs fast updates
    #  @param toUpdateServos An array containing the servo class objects
    def fastAPIUpdates(self,toUpdateServos):
        while self.running:
           try:
               self.updateServos(toUpdateServos)
               #send data to apps
               self.appServer.sendJSONToAll(self.getFastAPIJSON())
               sleep(0.5)
           except Exception, e:
               print "Timeout error in update API thread...", e

    ## Updates API info which needs slow updates
    def slowAPIUpdates(self):
        while self.running:
           try:
               #send data to apps
               self.appServer.sendJSONToAll(self.getSlowAPIJSON())
               sleep(5)
           except Exception, e:
               print "Error in update slow API thread...", e

## Camera frames for livestream
#  @param camera the camera class
def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

## REST API for getting servo information and a live stream.
#  Build with Flask web server.
class RestAPI(object):
    app = Flask(__name__)
    def __init__(self,mainprogram):
        self.mainprogram = mainprogram

    ## Index page for browsers
    @app.route('/')
    def index():
        """Video streaming home page."""
        return render_template('index.html')

    ## REST API
    @app.route('/api')
    def api():
        infoJSON = {"servos":[]}
        for servo in mainprogram.servos:
            infoJSON["servos"].append(
            {
                "id":servo.getId(),
                "temperature": servo.getTemperature(),
                "load": servo.getLoad(),
                "voltage": servo.getVoltage(),
                "position":servo.getPosition(),
                "moving": servo.getMovingStatus()
            })
        return str(infoJSON) #str(json.dumps(infoJSON, separators=(',',':'))#getJSON()

    ## Live stream
    @app.route('/video_feed')
    def video_feed():
        """Video streaming route. Put this in the src attribute of an img tag."""
        return Response(gen(Camera()),
                        mimetype='multipart/x-mixed-replace; boundary=frame')

    ## Starts the webserver for the REST API and livestream
    def start(self):
    	if __name__ == '__main__':
            self.app.run(host='0.0.0.0',debug=False,threaded=True)# to enable multithreading

if __name__ == '__main__':
    mainprogram = MainProgram()
    mainprogram.start()
    print "done...."
