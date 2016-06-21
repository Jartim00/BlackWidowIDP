from ax import Ax12
ax = Ax12()

## Servo wrapper for servo data.
#  This is used for the REST API and app server.
class Servo(object):

    ## The id the servo has been given.
    def __init__(self,id):
        self.id = id
        self.position = 0
        self.load = 0
        self.voltage = 0
        self.temperature = 0
        self.moving = 0

    ## Returns the id
    def getId(self):
        return self.id

    ## Returns the position from 0 through 1024
    def getPosition(self):
        return self.position

    ## Returns the load
    def getLoad(self):
        return self.load

    ## Returns the voltage
    def getVoltage(self):
        return self.voltage

    ## Returns the temperature
    def getTemperature(self):
        return self.temperature

    ## Returns the moving status: True when moving
    def getMovingStatus(self):
        return self.moving

    ## Updates all variables of the class
    def updateVariables(self):
        self.position = ax.readPosition(self.id)
        #print "position: ",position
        self.load = ax.readLoad(self.id)
        self.voltage = ax.readVoltage(self.id)
        self.temperature = ax.readTemperature(self.id)
        self.moving = ax.readMovingStatus(self.id)
