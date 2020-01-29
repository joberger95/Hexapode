import itertools
import time
import numpy
import pypot.dynamixel
import math

#Déclaration des 3 longueurs composant la patte en mm
L1= 54.0
L2= 68.0
L3= 135.0

theta2Correction = 14.0
theta3Correction = -theta2Correction + 47.0

#Coordonnées de P3: 
X3=float(input("X3="))
Y3=float(input("Y3="))
Z3=float(input("Z3="))

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
    
theta1 = math.atan2(Y3, X3)

xp = math.sqrt(X3*X3+Y3*Y3)-L1
if (xp < 0) :
    print("Destination trop prete")
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

#Affichage des angles en degres permettant d'obtenir P3
print("Valeur de theta1 : " ,theta1)
print("Valeur de theta2 : ", theta2)
print("Valeur de theta3 : ", theta3)

# Definition du port et du baudrate
dxl_io= pypot.dynamixel.DxlIO('/dev/ttyACM0', baudrate=1000000)  
dxl_io.set_goal_position({61:0})
dxl_io.set_goal_position({62:0})
dxl_io.set_goal_position({63:0})
time.sleep(5)
# Scan l'id du servomoteur
found_ids = [61,62,63]

# Création d'un tableau contenant les positions des servomoteurs
pos = dict(zip(found_ids, itertools.repeat(0)))

dxl_io.set_goal_position({61:theta1})
dxl_io.set_goal_position({62:theta2})
dxl_io.set_goal_position({63:theta3})

print("P3 : " ,X3,";", Y3,";", Z3)
print ("Angles pour P3 --> ", computeIK(X3, Y3, Z3, l1=L1, l2=L2,l3=L3))
time.sleep(0.1)