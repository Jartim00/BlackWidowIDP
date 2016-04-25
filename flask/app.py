#!/usr/bin/python
from flask import Flask, render_template, Response
from camera import Camera
import json

class MainProgram(object):
    def __init__(self):
        self.temperature = 60

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
        infoJSON = {'information':[{'temperature': mainprogram.temperature, 'hasses' : 'Willem'},{'temperature': mainprogram.temperature, 'hasses' : 'Willem'},{'temperature': mainprogram.temperature, 'hasses' : 'Willem'}]}
        mainprogram.temperature += 1
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
