import math

constL1 = 54.8
constL2 = 65.3
constL3 = 133

theta2Correction = 16.0
theta3Correction = -theta2Correction + 43.76

def alKashi(a, b, c):
    value = ((a*a)+(b*b)-(c*c))/(2*a*b)
    return -math.acos(value)

def computeDK(theta1, theta2, theta3, l1=constL1, l2=constL2,l3=constL3) :
    theta1 = theta1 * math.pi / 180.0
    theta2 = (theta2 - theta2Correction) * math.pi / 180.0
    theta3 = (theta3 - theta3Correction) * math.pi / 180.0
    print("corrected angles={}, {}, {}".format(theta1*180.0/math.pi, theta2*180.0/math.pi, theta3*180.0/math.pi))

    planContribution = l1 + l2*math.cos(theta2) + l3*math.cos(theta2 + theta3)

    x = math.cos(theta1) * planContribution
    y = math.sin(theta1) * planContribution
    z = -(l2 * math.sin(theta2) + l3 * math.sin(theta2 + theta3))

    return [x, y, z]

def computeIK(leg_id,x, y, z, l1=constL1, l2=constL2,l3=constL3) :
    theta1 = math.atan2(y, x)

    xp = math.sqrt(x*x+y*y)-l1
    if (xp < 0) :
        print("Destination point too close")
        xp = 0

    d = math.sqrt(math.pow(xp,2) + math.pow(z,2))
    if (d > l2+l3):
        print("Destination point too far away")
        d = l2+l3

    theta2 = -(alKashi(l2, d, l3) + math.atan2(z, xp))
    theta3 = math.pi - alKashi(l2, l3, d)

    if(leg_id==1 or leg_id==5 or leg_id==6):
        theta1 = modulo180(math.degrees(theta1))
        theta2 = modulo180(math.degrees(theta2) + theta2Correction)
        theta3 = modulo180(math.degrees(theta3) + theta3Correction)

    if(leg_id==2 or leg_id==3 or leg_id==4):
        theta1 = modulo180(math.degrees(theta1))
        theta2 = -modulo180(math.degrees(theta2) + theta2Correction)
        theta3 = -modulo180(math.degrees(theta3) + theta3Correction)

    return theta1,theta2,theta3
    
def modulo180(angle) :
    if (-180 < angle < 180) :
        return angle

    angle  = angle % 360
    if (angle > 180) :
        return -360 + angle

    return angle

def main():
    print ("0, 0, 0 --> ", computeDK(0, 0, 0, l1=constL1, l2=constL2,l3=constL3))
    print ("90, 0, 0 --> ", computeDK(90, 0, 0, l1=constL1, l2=constL2,l3=constL3))
    print ("180, -30.501, -67.819 --> ", computeDK(180, -30.501, -67.819, l1=constL1, l2=constL2,l3=constL3))
    print ("0, -30.645, 38.501 --> ", computeDK(0, -30.645, 38.501, l1=constL1, l2=constL2,l3=constL3))

if __name__ == '__main__' :
    main()
