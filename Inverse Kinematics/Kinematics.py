import math

class IK:

    tibia = 124
    femur = 78
    coxa = 37
    offset = 71
    servo_beta = 0
    servo_alpha = 0


    def calc_angles_debug(self,x,y,z):
        L1 = math.sqrt(x**2+ y**2)
        print "L1: ",L1
        gama = math.atan(x/y)/math.pi * 180
        print "Gama: ",gama
        L = math.sqrt(((L1 - self.coxa)**2)+z**2)
        print "L: ", L
        beta = math.acos((self.tibia**2 + self.femur**2 - L ** 2)/ (2*self.tibia*self.femur)) / math.pi * 180
        print "beta: ",beta
        alpha1 = math.acos(z/L)/math.pi*180
        print "alpha1: ",alpha1
        alpha2 = math.acos((self.femur**2+ L**2 - self.tibia**2)/(2*self.femur*L)) / math.pi * 180
        print "alpha2: ",alpha2
        alpha = alpha1 + alpha2
        print "alpha: ",alpha
        self.servo_beta = 180 - beta
        print "beta in servo angle: ", 180 - beta
        self.servo_alpha = alpha2 - (math.atan(self.offset/(L1-self.coxa)) / math.pi * 180)
        print "alpha in servo angle: ", alpha2 - (math.atan(self.offset/(L1-self.coxa)) / math.pi * 180)

    def calc_angles(self,x,y,z):
        L1 = math.sqrt(x ** 2 + y ** 2)
        L = math.sqrt(((L1 - self.coxa) ** 2) + z ** 2)
        beta = math.acos((self.tibia ** 2 + self.femur ** 2 - L ** 2) / (2 * self.tibia * self.femur)) / math.pi * 180
        alpha2 = math.acos((self.femur ** 2 + L ** 2 - self.tibia ** 2) / (2 * self.femur * L)) / math.pi * 180
        self.servo_alpha = alpha2 - (math.atan(self.offset / (L1 - self.coxa)) / math.pi * 180)
        self.servo_beta = 180 - beta
        return [self.servo_alpha,self.servo_beta]

    def __init__(self):
        pass


offset = 71
print IK().calc_angles( 119.1401242, 84.24478972, offset)  # stap pos hoekpoot
print IK().calc_angles( 0, 84.24478972, offset)  # default pos hoekpoot
print IK().calc_angles( 0, 103.1783, offset)  # default pos middenpoot
IK().calc_angles_debug(119.1401242, 103.1783, offset)  # stap pos middenpoot