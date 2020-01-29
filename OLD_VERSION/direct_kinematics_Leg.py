import itertools
import time
import numpy
import pypot.dynamixel
import math


if __name__ == '__main__':


    l1 = 54
    l2 = 67
    l3 = 134
    theta1 = float(input("Saisissez Theta1 : "))
    theta2 = float(input("Saisissez Theta2 : "))
    theta3 = float(input("Saisissez Theta3 : "))
    
    #Conversion des degrés en radians /!\
    Theta2c= 14.0
    Theta3c= -Theta2c+47.0
    theta2 = theta2-Theta2c
    theta3 = (theta3-Theta3c)
    #Conversion des angles en radians
    theta1=math.radians(theta1)
    theta2=math.radians(theta2)
    theta3=math.radians(theta3)

    x3= math.cos(theta1)*(l1+l2*math.cos(theta2)+l3*math.cos(theta2+theta3))
    y3= math.sin(theta1)*(l1+l2*math.cos(theta2)+l3*math.cos(theta2+theta3))
    z3= l2*math.sin(theta2)+l3*math.sin(theta2+theta3)

    theta1=theta1*180/math.pi
    theta2=theta2*180/math.pi
    theta3=theta3*180/math.pi
        



    # Definition du port et du baudrate
    dxl_io= pypot.dynamixel.DxlIO('/dev/ttyACM1', baudrate=1000000)  
    # Scan l'id du servomoteur
    found_ids = [61,62,63] # this may take several seconds
    #found_ids.pop(253)
    print ("Detected:", found_ids)

    found_ids=found_ids[:-1]
    print(found_ids)

    # Recupere la position 
    print ("Current pos:", dxl_io.get_present_position(found_ids))

    # we create a python dictionnary: {id0 : position0, id1 : position1...}
    pos = dict(zip(found_ids, itertools.repeat(0)))
    print ("Cmd:", pos)

    # we send these new positions
    dxl_io.set_goal_position({61:theta1})
    dxl_io.set_goal_position({62:theta2})
    dxl_io.set_goal_position({63:theta3})
    time.sleep(1)  # pause

    # we get the current positions
    #print ("New pos:", dxl_io.get_present_position(found_ids))
    print("P3 : " ,x3,";", y3,";", z3)

    dxl_io.disable_torque(found_ids)
    
    time.sleep(0.1)  # Pause