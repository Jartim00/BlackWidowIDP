#!/usr/bin/python
from flask import Flask
#import moduletest
import json
class MainProgram(object):
    def __init__(self):
        self.temperature = 60
class RestAPI(object):
    app = Flask(__name__)
    def __init__(self,mainprogram):
        self.mainprogram = mainprogram

    @app.route('/')
    def index():
        infoJSON = {'information':[{'temperature': mainprogram.temperature, 'hasses' : 'Willem'},{'temperature': mainprogram.temperature, 'hasses' : 'Willem'},{'temperature': mainprogram.temperature, 'hasses' : 'Willem'}]}
        mainprogram.temperature += 1
        return str(infoJSON)#getJSON()

    @app.route('/video')
    def video():
        return "video"

    def start(self):
    	if __name__ == '__main__':
            self.app.run(host='0.0.0.0')
    	else:
            print "You are running as a module"
            self.app.run(host='0.0.0.0')
mainprogram = MainProgram()
restapi = RestAPI(mainprogram)
restapi.start()
print "done...."
