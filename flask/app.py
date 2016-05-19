#!/usr/bin/python
from flask import Flask, render_template, Response
from camera import Camera
import json
import threading
from time import sleep
from ax import Ax12
ax = Ax12()

class Servo(object):
    def __init__(self,id):
        self.id = id
        self.position = 0
        self.load = 0
        self.voltage = 0
        self.temperature = 0
        self.moving = 0

    def getId(self):
        return self.id

    def getPosition(self):
        return self.position

    def getLoad(self):
        return self.load

    def getVoltage(self):
        return self.voltage

    def getTemperature(self):
        return self.temperature

    def getMovingStatus(self):
        return self.moving

    def updateVariables(self):
        self.position = ax.readPosition(self.id)
        self.load = ax.readLoad(self.id)
        self.voltage = ax.readVoltage(self.id)
        self.temperature = ax.readTemperature(self.id)
        self.moving = ax.readMovingStatus(self.id)

class MainProgram(object):
    servos = []
    def __init__(self):
        self.createServos(6,3)
        self.startUpdateThread()

    def createServos(self,numLegs,servosPerLeg):
        if not 1 <= servosPerLeg <= 9:
            return
        self.servos = [Servo(servoId) for servoId in ax.learnServos(10,70)]
        '''for legNum in range(10,(numLegs + 1) * 10,10):
            for servoNum in range(1,servosPerLeg+1):
                #create servo
                servoId = legNum + servoNum
                self.servos.append(Servo(servoId))'''

    def startUpdateThread(self):
        t = threading.Thread(target=self.updateServos)
        t.start()

    def updateServos(self):
        while True:
            try:
                for servo in self.servos:
                    servo.updateVariables()
                sleep(5)
            except KeyboardInterrupt:
                break

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

class RestAPI(object):
    app = Flask(__name__)
    def __init__(self,mainprogram):
        self.mainprogram = mainprogram

    @app.route('/')
    def index():
        """Video streaming home page."""
        return render_template('index.html')

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
        return str(infoJSON)#getJSON()

    @app.route('/video_feed')
    def video_feed():
        """Video streaming route. Put this in the src attribute of an img tag."""
        return Response(gen(Camera()),
                        mimetype='multipart/x-mixed-replace; boundary=frame')

    def start(self):
    	if __name__ == '__main__':
            self.app.run(host='0.0.0.0',debug=True)#threaded=True to enable multithreading
mainprogram = MainProgram()
restapi = RestAPI(mainprogram)
restapi.start()
print "done...."
