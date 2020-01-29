import pypot.dynamixel
import numpy  
import kinematics

#Analyse des ports
ports=pypot.dynamixel.get_available_ports()

#Creation de la connexion serie
with pypot.dynamixel.DxlIO(ports[0], baudrate=1000000)  as dxl_io :
    #scan du robot
    angles=kinematics.computeIK(160,0,90)

    for i in [1,2,3,4,5,6]:
        print("Initialisatin des pattes: ")
        ids=[i*10+1, i*10+2, i*10+3]
        dxl_io.set_goal_position({ids[0]:angles[0] , ids[1]:angles[1] ,ids[2]:angles[2]})
        print("Patte",i,"initialisee")