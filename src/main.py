#!/usr/bin/python
from flask import Flask, render_template, Response, request
from camera_pi import Camera
import json
import threading
from multiprocessing import Process
from servo import Servo
from time import sleep
from ax import Ax12
ax = Ax12()

class MainProgram(object):
    servos = []
    def __init__(self):
        print "Main...."
        self.createServos(6,3)
        print "Main end..."

    def start(self):
        self.running = True
        self.startUpdateThread()
        #continuous updates
        while self.running:
            try:
                print "another loop..."
                sleep(1)
            except KeyboardInterrupt:
                print "exiting mainprogram..."
                self.shutdown()
                return

    def shutdown(self):
        self.running = False
        #shutdown flask
        #self.apiserver.terminate()
        #self.apiserver.join()
        # self.shutdown_server()

    # def shutdown_server(self):
    #     func = request.environ.get('werkzeug.server.shutdown')
    #     if func is None:
    #         raise RuntimeError('Not running with the Werkzeug Server')
    #     func()

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
        print "starting update thread..."
        threading.Thread(target=self.updateServos,args=(self.servos,)).start()
        restapi = RestAPI(self)
        self.apiserver = threading.Thread(target=restapi.start)
        self.apiserver.daemon = True
        self.apiserver.start()

    def updateServos(self,toUpdateServos):
        while self.running:
           try:
               print "updating servos..."
               for servo in toUpdateServos:
                   try:
                       servo.updateVariables()
                   except ax.timeoutError:
                       print "error...."
               sleep(1)
           except:
               print "Timeout error in update servo thread..."

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
            self.app.run(host='0.0.0.0',debug=False)#threaded=True to enable multithreading
if __name__ == '__main__':
    mainprogram = MainProgram()
    mainprogram.start()
    print "done...."