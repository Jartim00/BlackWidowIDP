import math

tibia = 124
femur = 78
coxa = 37
offset = 71
servo_beta = 0
servo_alpha = 0

def calc_angles_debug(x,y,z):
    L1 = math.sqrt(x**2+ y**2)
    print "L1: ",L1
    gama = math.atan(x/y)/math.pi * 180
    print "Gama: ",gama
    L = math.sqrt(((L1 - coxa)**2)+z**2)
    print "L: ", L
    beta = math.acos((tibia**2 + femur**2 - L ** 2)/ (2*tibia*femur)) / math.pi * 180
    print "beta: ",beta
    alpha1 = math.acos(z/L)/math.pi*180
    print "alpha1: ",alpha1
    alpha2 = math.acos((femur**2+ L**2 - tibia**2)/(2*femur*L)) / math.pi * 180
    print "alpha2: ",alpha2
    alpha = alpha1 + alpha2
    print "alpha: ",alpha
    servo_beta = 180 - beta
    print "beta in servo angle: ", 180 - beta
    servo_alpha = alpha2 - (math.atan(offset/(L1-coxa)) / math.pi * 180)
    print "alpha in servo angle: ", alpha2 - (math.atan(offset/(L1-coxa)) / math.pi * 180)

def calc_angles(x,y,z):
    global servo_alpha
    global servo_beta
    L1 = math.sqrt(x ** 2 + y ** 2)
    L = math.sqrt(((L1 - coxa) ** 2) + z ** 2)
    beta = math.acos((tibia ** 2 + femur ** 2 - L ** 2) / (2 * tibia * femur)) / math.pi * 180
    alpha2 = math.acos((femur ** 2 + L ** 2 - tibia ** 2) / (2 * femur * L)) / math.pi * 180
    servo_alpha = alpha2 - (math.atan(offset / (L1 - coxa)) / math.pi * 180)
    servo_beta = 180 - beta


calc_angles(119.1401242,84.24478972,offset)

print servo_alpha, " : ", servo_beta

calc_angles(0, 84.24478972, offset)

print servo_alpha, " : ", servo_beta