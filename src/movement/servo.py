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
        #print "position: ",position
        self.load = ax.readLoad(self.id)
        self.voltage = ax.readVoltage(self.id)
        self.temperature = ax.readTemperature(self.id)
        self.moving = ax.readMovingStatus(self.id)
