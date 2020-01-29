import pypot.dynamixel
import numpy 
import calcul 
import time
import kinematics

#Creation des ports et du dxl_io
#Analyse des ports et ouverture de la liaison série
#ports=pypot.dynamixel.get_available_ports()
#with pypot.dynamixel.DxlIO(ports[0], baudrate=1000000)  as dxl_io :
    #print("DXL_IO= ",dxl_io)
    
#Initialisation a une position initiale
def init_pos():
    for i in [1,2,3,4,5,6]:
        angles=kinematics.computeIK(i,180,0,90)
        print("Initialisatin des pattes: ")
        ids=[i*10+1, i*10+2, i*10+3]
        dxl_io.set_goal_position({ids[0]:angles[0] , ids[1]:angles[1] ,ids[2]:angles[2]})
        print("Patte",i,"initialisee")   


#Creation du tableau de positions    
leg_init_pos=[160,-40,90]

def calculate_next_point(dx,dy,dz,mt,a):   
    ########### Go Forward ########### 
    x=leg_init_pos[0]
    y=leg_init_pos[1]
    z=leg_init_pos[2]
   
   
    if mt==0:  
        if a==0:
            print("Boucle 1")
            leg_delta=[ dx , dy , -dz]
            leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
            leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
            leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
            y=leg_init_pos[1]
            z=leg_init_pos[2]
            if y==0 :
                print("Leg_init_pos=",leg_init_pos)
                a=1
            return a
        if a==1:
            a=1
            print("Boucle 2")
            leg_delta=[ dx , dy , dz]
            leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
            leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
            leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
            y=leg_init_pos[1]
            z=leg_init_pos[2]
            if y==40 and z==90:
                a=2
        if a==2:
            a=2
            print("Boucle 3")
            leg_delta=[ dx , -4*dy , 0]
            y=leg_init_pos[1]
            z=leg_init_pos[2]
            if y==-40 and z==90:
                a=0
    """########### Go back ###########  
    if mt==1:    
        if y<=40 and z<=0:
            leg_delta=[ x , -y , -z ]
            leg_final_pos[j]=leg_init_pos[i][j]+(leg_delta[j])
        if y<=0 and z<=90:
            leg_delta=[ x , -y , z ]
            leg_final_pos[j]=leg_init_pos[i][j]+(leg_delta[j])
        if z>91:
            leg_delta=[ x , 4*y , 0 ]
            leg_final_pos[j]=leg_init_pos[i][j]+(leg_delta[j])
        if y==41 and z>91:
            leg_delta=[ x , -y , -z  ]
            leg_final_pos[j]=leg_init_pos[i][j]+(leg_delta[j])

    ########### Go left ###########    
    if mt==2:    
        if x<=155 and z<=0:
            leg_delta=[ x , y , -z  ]
            leg_final_pos[j]=leg_init_pos[i][j]+(leg_delta[j])
        if x<=170 and z<=90:
            leg_delta=[ x , y , z ]
            leg_final_pos[j]=leg_init_pos[i][j]+(leg_delta[j])
        if z>90:
            leg_delta=[ -3*x , y , 0  ]
            leg_final_pos[j]=leg_init_pos[i][j]+(leg_delta[j])
        if x==140 and z<90:
            leg_delta=[ x , y , -z ]
            leg_final_pos[j]=leg_init_pos[i][j]+(leg_delta[j])

    ########### Go right ###########       
    if mt==3:    
        if x<=155 and z<=0:
            leg_delta=[ x , y , -z ]
            leg_final_pos[j]=leg_init_pos[i][j]+(leg_delta[j])
        if x<=170 and z<=90:
            leg_delta=[ x , y , z ]
            leg_final_pos[j]=leg_init_pos[i][j]+(leg_delta[j])
        if z>90:
            leg_delta=[ -3*x , y , 0 ]
            leg_final_pos[j]=leg_init_pos[i][j]+(leg_delta[j])
        if x==140 and z<90:
            leg_delta=[ x , y , -z ]
            leg_final_pos[j]=leg_init_pos[i][j]+(leg_delta[j])"""
    for i in[0,1,2]:
        print("\n",leg_init_pos[i])
        print("a=",a)

def set_goal_position():            
    dx=leg_final_pos[0]
    dy=leg_final_pos[1]
    dz=leg_final_pos[2]
    print("dx=",dx,"dy=",dy,"dz=",dz)
    for i in [1,2,3,4,5,6]:
        leg_id=i
        calcul.set_leg_pos_robot_frame(leg_id,dx,dy,dz)

        
def set_leg_pos(leg_id,x,y,z):
    id1=leg_id*10+1
    id2=leg_id*10+2
    id3=leg_id*10+3
    angles=kinematics.computeIK(leg_id,x,y,z)  
    ports=pypot.dynamixel.get_available_ports()
    with pypot.dynamixel.DxlIO(ports[0], baudrate=1000000)  as dxl_io :
        dxl_io.set_goal_position({id1:angles[0],id2:angles[1],id3:angles[2]})