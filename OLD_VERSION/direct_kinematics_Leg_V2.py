import itertools
import time
import numpy
import pypot.dynamixel
import math


if __name__ == '__main__':

    l1 = 54.0
    l2 = 68.0
    l3 = 135.0
    
    # Definition du port et du baudrate
    dxl_io= pypot.dynamixel.DxlIO('/dev/ttyACM0', baudrate=1000000)  
    # Scan l'id du servomoteur
    found_ids = [41,42,43]  # this may take several seconds
    #found_ids.pop(253)
    print ("Detected:", found_ids)
    print(found_ids)

    dxl_io.disable_torque(found_ids)
    while True:
        #print ("Current pos:", dxl_io.get_present_position(found_ids))
        
        #Injection des thetas pour les calculs
        theta1F = dxl_io.get_present_position([41])
        theta2F = dxl_io.get_present_position([42])
        theta3F = dxl_io.get_present_position([43])
        #print(theta3F)
        theta1=theta1F[0]
        theta2=theta2F[0] 
        theta3=theta3F[0] 
        print("Angles lus:",theta1,";",theta2,";",theta3)

        Theta2c= 14.0
        Theta3c= -Theta2c+47.0
        theta2 = theta2-Theta2c
        theta3 = (theta3-Theta3c)
        #Conversion des angles en radians
        theta1=math.radians(theta1)
        theta2=math.radians(theta2)
        theta3=math.radians(theta3)

        print("Angles corrigés:",theta1*180/math.pi,";",theta2*180/math.pi,";",theta3*180/math.pi)


        x3= math.cos(theta1)*(l1+l2*math.cos(theta2)+l3*math.cos(theta2+theta3))
        y3= math.sin(theta1)*(l1+l2*math.cos(theta2)+l3*math.cos(theta2+theta3))
        z3= -(l2*math.sin(theta2)+l3*math.sin(theta2+theta3))

        #Affichage de P3
        print("X,Y,Z de P3 : " ,x3 ,";", y3,";", z3,"\n")

        #delay
        time.sleep(2) 