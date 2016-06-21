MAX_OUTER_ANGLE_CORNER = 45
MAX_OUTER_ANGLE_MID = 25
MIN_BASE_ANGLE_STEP = 9.73

def move(self, speed, rotationAngle):

  if not -512 <= speed <= 512:
      raise Exception("Speed beyond limits")
  if speed < 0 :
    moveBackward(abs(speed),rotationAngle)
  else:
    moveForward(speed,rotationAngle)

def moveForward(self, speed, rotationAngle):
    angle = 0


    angle = 9.73 + self.calculateDOF(rotationAngle)
    angle = -9.73 + self.calculateDOF(rotationAngle)




def moveBackward(self, speed, rotationAngle):



def calculateDOF(leg,rotationAngle):
    #return (45 - 9.73) / 512.0 * rotationAngle
    if leg in [1,3,4,6]:
        return abs(MAX_OUTER_ANGLE_CORNER) + MIN_BASE_ANGLE_STEP + ((MAX_OUTER_ANGLE_CORNER - abs(MIN_BASE_ANGLE_STEP) * abs(rotationAngle)))
    else:
        return 2 * MAX_OUTER_ANGLE_MID
