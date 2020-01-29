import itertools
import time
import numpy
import pypot.dynamixel
import math

#Déclaration des 3 longueurs composant la patte en mm
L1= 55
L2= 68
L3= 135

theta2Correction = 14
theta3Correction = -theta2Correction + 47

# Definition du port et du baudrate
dxl_io= pypot.dynamixel.DxlIO('/dev/ttyACM0', baudrate=1000000)
#dxl_io.set_goal_position({61:0})
#dxl_io.set_goal_position({62:0})
#dxl_io.set_goal_position({63:0})
#time.sleep(2)

# Scan l'id du servomoteur
#found_ids = dxl_io.scan()
found_ids=[11, 12, 13, 21, 22, 23, 31, 32, 33, 41, 42, 43, 51, 52, 53, 61, 62, 63]
#found_ids=found_ids[:-1]

def alKashi(a,b,c):
    value=((a*a)+(b*b)-(c*c))/(2*a*b)
    return -math.acos(value)

def modulo180(angle) :
    if (-180 < angle < 180) :
        return angle

    angle  = angle % 360
    if (angle > 180) :
        return -360 + angle

    return angle

def computeIK(x, y, z, l1=L1, l2=L2,l3=L3) :

    theta1 = math.atan2(y, x)
    
    xp = math.sqrt(x*x+y*y)-l1
    if (xp < 0) :
        print("Destination trop prete")
        xp = 0

    d = math.sqrt(math.pow(xp,2) + math.pow(z,2))
    if (d > l2+l3):
        print("Destination trop loin")
        d = l2+l3

    theta2 = -(alKashi(l2, d, l3) + math.atan2(z, xp))
    theta3 = -math.pi - alKashi(l2, l3, d)

    return [modulo180(math.degrees(theta1)), modulo180(math.degrees(theta2) + theta2Correction), modulo180(math.degrees(theta3) + theta3Correction)]

'''-----'''
#Defintion du centre du cercle
centreX=200
centreY=0
Z3=0
angleres=1
radius=30
d_angle= angleres*math.pi/180
anglecercle=0
while True:
    for i in range(1,360):
        anglecercle = anglecercle + d_angle
        X3=centreX+radius*math.cos(anglecercle)
        Y3=centreY+radius*math.sin(anglecercle)

        theta1 = math.atan2(Y3, X3)

        xp = math.sqrt(X3*X3+Y3*Y3)-L1
        if (xp < 0) :
            print("Destination trop proche")
            xp = 0

        d = math.sqrt(math.pow(xp,2) + math.pow(Z3,2))
        if (d > L2+L3):
            print("Destination trop loin")
            d = L2+L3

        theta2 = -(alKashi(L2, d, L3) + math.atan2(Z3, xp))
        theta3 = -math.pi - alKashi(L2, L3, d)

        theta1=modulo180(math.degrees(theta1))
        theta2=modulo180(math.degrees(theta2) + theta2Correction)
        theta3=modulo180(math.degrees(theta3) + theta3Correction)
        '''---'''
        """
        #Affichage des angles en degres permettant d'obtenir P3
        print("Valeur de theta1 : " ,theta1)
        print("Valeur de theta2 : ", theta2)
        print("Valeur de theta3 : ", theta3)
        """
        dxl_io.set_goal_position({21:-theta1})
        dxl_io.set_goal_position({22:theta2})
        dxl_io.set_goal_position({23:theta3})
        dxl_io.set_goal_position({61:theta1})
        dxl_io.set_goal_position({62:theta2})
        dxl_io.set_goal_position({63:theta3})
        dxl_io.set_goal_position({31:-theta1})
        dxl_io.set_goal_position({32:-theta2})
        dxl_io.set_goal_position({33:-theta3})
        dxl_io.set_goal_position({11:theta1})
        dxl_io.set_goal_position({12:-theta2})
        dxl_io.set_goal_position({13:-theta3})
        dxl_io.set_goal_position({41:-theta1})
        dxl_io.set_goal_position({42:-theta2})
        dxl_io.set_goal_position({43:-theta3})
        dxl_io.set_goal_position({51:theta1})
        dxl_io.set_goal_position({52:-theta2})
        dxl_io.set_goal_position({53:-theta3})
        #print("P3 : " ,X3,";", Y3,";", Z3)
        #print ("Angles pour P3 --> ", computeIK(X3, Y3, Z3, l1=L1, l2=L2,l3=L3))
        time.sleep(0.005)