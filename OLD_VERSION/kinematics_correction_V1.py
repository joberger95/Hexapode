import math

constL1 = 54
constL2 = 67
constL3 = 134

theta2Correction = 14
theta3Correction = -theta2Correction + 47


def alKashi(a, b, c):
    value = ((a*a)+(b*b)-(c*c))/(2*a*b)
    return -math.acos(value)


def computeDK(theta1, theta2, theta3, l1=constL1, l2=constL2,l3=constL3) :
    theta1 = theta1 * math.pi / 180.0
    theta2 = (theta2 - theta2Correction) * math.pi / 180.0
    theta3 = (theta3 - theta3Correction) * math.pi / 180.0

    planContribution = l1 + l2*math.cos(theta2) + l3*math.cos(theta2 + theta3)

    x = math.cos(theta1) * planContribution
    y = math.sin(theta1) * planContribution
    z = -(l2 * math.sin(theta2) + l3 * math.sin(theta2 + theta3))

    return [x, y, z]


def computeIK(x, y, z, l1=constL1, l2=constL2,l3=constL3) :
    
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
    theta3 = -math.pi - alKashi(l2, l3, d)

    return [modulo180(math.degrees(theta1)), modulo180(math.degrees(theta2) + theta2Correction), modulo180(math.degrees(theta3) + theta3Correction)]

def modulo180(angle) :
    if (-180 < angle < 180) :
        return angle

    angle  = angle % 360
    if (angle > 180) :
        return -360 + angle

    return angle

def main():
    print ("0, 39, -56 --> ", computeDK(0, 39, -56, l1=constL1, l2=constL2,l3=constL3))
    print ("180, 0, 90 --> ", computeIK(180, 0, 90, l1=constL1, l2=constL2,l3=constL3))
    print("------")

if __name__ == '__main__' :
    main()
