import pypot.dynamixel
import numpy 
import calcul 
import time
import kinematics
import math

#Creation des ports et du dxl_io
#Analyse des ports et ouverture de la liaison série
ports=pypot.dynamixel.get_available_ports()
dxl_io= pypot.dynamixel.DxlIO(ports[0], baudrate=1000000) 
found_ids=dxl_io.scan()
found_ids=found_ids[:-1]
npattes=int(len(found_ids)/3)
#     print("DXL_IO= ",dxl_io)
#     print("Initialisatin des pattes: ")
#     for i in [1,2,3,4,5,6]:            
#         ids=[i*10+1, i*10+2, i*10+3]
#         angles=kinematics.computeIK(ids,160,-40,90)
#         dxl_io.set_goal_position({ids[0]:angles[0] , ids[1]:angles[1] ,ids[2]:angles[2]})
#         print("Patte",i,"initialisee")  

  
a=0
def next_point(dx,dy,dz,mt):
    ports=pypot.dynamixel.get_available_ports()
    with pypot.dynamixel.DxlIO(ports[0], baudrate=1000000)  as dxl_io :
        global a
        #Recuperation de la position en x,y,z d'une patte
        for i in [1,3,5]:
            ids=i
            x=dxl_io.get_present_position([ids*10+1])
            y=dxl_io.get_present_position([ids*10+2])
            z=dxl_io.get_present_position([ids*10+3])
            x=x[0]
            y=y[0]
            z=z[0]
            kinematics.computeDK(x,y,z)
            
            #Ajout de la derivee a la position de la patte
            #Exemple: ny= nouvelle valeur, y=valeur lue sur la patte, dy=valeur a ajouter
            #mutliplication par sin(mt)
            # Si mt=0--> nx=x+dx*math.sin(mt) => nx=x
            nx=x+dx*math.sin(mt)
            ny=y+dy*math.sin(mt)
            nz=z+dz*math.sin(mt)
            print("nx=",nx)
            print("ny=",ny)
            print("nz=",nz)
            #Envoi des nouvelles positions pour le deplacement du robot
            calcul.set_leg_pos_robot_frame(ids,nx,ny,nz)



##################################################################

leg_init_pos1=[160,-40,90]
leg_init_pos2=[160,0,0]
b=0

def default():
    for i in [1,2,3,4,5,6]:
        print("Initialisatin des pattes: ")
        angles=kinematics.computeIK(i,160,-40,90)
        ids=[i*10+1, i*10+2, i*10+3]
        dxl_io.set_goal_position({ ids[0]:angles[0] , ids[1]:angles[1] , ids[2]:angles[2]})
        print("Patte",i,"initialisee")

def anglelimit():
    print("Definition des angles limites")
    b=0
    for i in range (npattes):
        dxl_io.set_angle_limit({found_ids[b]:(-107,107)})
        dxl_io.set_angle_limit({found_ids[b+1]:(-107,107)})
        dxl_io.set_angle_limit({found_ids[b+2]:(-138,91)})
        b=b+3

def calculate_next_point(dx,dy,dz,mt,b_offset=0):   
    ########### Go Forward ########### 
    global b, leg_init_pos1,leg_init_pos2
    print(b)
    margin=1

    if b_offset==0:
        leg_init_pos=leg_init_pos1
        x=leg_init_pos[0]
        y=leg_init_pos[1]
        z=leg_init_pos[2]
    else:
        leg_init_pos=leg_init_pos2
        x=leg_init_pos2[0]
        y=leg_init_pos2[1]
        z=leg_init_pos2[2]

    #Mise en place de l'offset
    bigb=(b+b_offset)%3
    #Boucles de déplacement du robot
    if mt==0:          
        if bigb==0:
            print("Boucle 1")
            leg_delta=[ dx , dy , -dz]
            leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
            leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
            leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
            y=leg_init_pos[1]
            z=leg_init_pos[2]
            print("b=",bigb)
            #updating global variable
            if b_offset==0:
                leg_init_pos1=leg_init_pos
            else:
                leg_init_pos2=leg_init_pos
                
            if abs(y-0)<margin :
                if b_offset!=0:
                    return
                print("Leg_init_pos=",leg_init_pos)
                b=(b+1)%3
                bigb=(b+b_offset)%3
                print("bigb=",bigb)
            return 

        if bigb==1:        
            print("bigboucle 2")
            leg_delta=[ dx , dy , dz]
            leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
            leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
            leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
            y=leg_init_pos[1]
            z=leg_init_pos[2]
            #updating global variable
            if b_offset==0:
                leg_init_pos1=leg_init_pos
            else:
                leg_init_pos2=leg_init_pos
                
            if abs(y-40)<margin and abs(z-90)<margin:
                if b_offset!=0:
                    return
                print("Leg_init_pos=",leg_init_pos)
                b=(b+1)%3
                bigb=(b+b_offset)%3
                print("bigb=",bigb)
            return

        if bigb==2:
            print("bigboucle 3")
            leg_delta=[ dx , -2*dy , 0]
            leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
            leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
            leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
            y=leg_init_pos[1]
            z=leg_init_pos[2]
            #updating global variable
            if b_offset==0:
                leg_init_pos1=leg_init_pos
            else:
                leg_init_pos2=leg_init_pos
                
            if abs(y+40)<margin and abs(z-90)<margin:
                if b_offset!=0:
                    return
                print("Leg_init_pos=",leg_init_pos)
                b=(b+1)%3
                bigb=(b+b_offset)%3
                print("bigb=",bigb)
            return
        
    ########### Go back ###########  
    # if mt==1:    
    #     if b==0:
    #         print("Boucle 1")
    #         leg_delta=[ dx , -dy , -dz]
    #         leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
    #         leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
    #         leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
    #         y=leg_init_pos[1]
    #         z=leg_init_pos[2]
    #         if y==0 :
    #             print("Leg_init_pos=",leg_init_pos)
    #             b=1
    #     if b==1:
    #         b=1
    #         print("Boucle 2")
    #         leg_delta=[ dx , -dy , dz]
    #         leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
    #         leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
    #         leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
    #         y=leg_init_pos[1]
    #         z=leg_init_pos[2]
    #         if y==-40 and z==90:
    #             print("Leg_init_pos=",leg_init_pos)
    #             b=2
    #     if b==2:
    #         b=2
    #         print("Boucle 3")
    #         leg_delta=[ dx , 2*dy , 0]
    #         leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
    #         leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
    #         leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
    #         y=leg_init_pos[1]
    #         z=leg_init_pos[2]
    #         if y==40 and z==90:
    #             print("Leg_init_pos=",leg_init_pos)
    #             b=0
    #     return b
    # if mt==1:          
    #     if bigb==0:
    #         print("Boucle 1")
    #         leg_delta=[ dx , dy , -dz]
    #         leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
    #         leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
    #         leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
    #         y=leg_init_pos[1]
    #         z=leg_init_pos[2]
    #         print("b=",bigb)
    #         if y==0 :
    #             if b_offset!=0:
    #                 return
    #             if b_offset==0:
    #                 print("Leg_init_pos=",leg_init_pos)
    #                 b=(b+1)%3
    #                 bigb=(b+b_offset)%3
    #                 print("bigb=",bigb)
    #         return 

    #     if bigb==1:        
    #         print("bigboucle 2")
    #         leg_delta=[ dx , dy , dz]
    #         leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
    #         leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
    #         leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
    #         y=leg_init_pos[1]
    #         z=leg_init_pos[2]
    #         if y==40 and z==90:
    #             if b_offset!=0:
    #                 return
    #             if b_offset==0:
    #                 print("Leg_init_pos=",leg_init_pos)
    #                 b=(b+1)%3
    #                 bigb=(b+b_offset)%3
    #         return

    #     if bigb==2:
    #         print("bigboucle 3")
    #         leg_delta=[ dx , -2*dy , 0]
    #         leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
    #         leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
    #         leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
    #         y=leg_init_pos[1]
    #         z=leg_init_pos[2]
    #         if y==-40 and z==90:
    #             if b_offset!=0:
    #                 return
    #             if b_offset==0:
    #                 print("Leg_init_pos=",leg_init_pos)
    #                 b=(b+1)%3
    #                 bigb=(b+b_offset)%3
    #         return
    
    # for i in[0,1,2]:
    #     print("\n",leg_init_pos[i])
    #     print("a=",a)

# def set_goal_position():            
#     dx=leg_init_pos[0]
#     dy=leg_init_pos[1]
#     dz=leg_init_pos[2]
#     print("dx=",dx,"dy=",dy,"dz=",dz)
#     for i in [1,2,3,4,5,6]:
#         leg_id=i
#         calcul.set_leg_pos_robot_frame(leg_id,dx,dy,dz) 


def set_goal_position1():            
    dx=leg_init_pos1[0]
    dy=leg_init_pos1[1]
    dz=leg_init_pos1[2]
    print("dx=",dx,"dy=",dy,"dz=",dz)
    for i in [1,3,5]:
        leg_id=i
        calcul.set_leg_pos_robot_frame(leg_id,dx,dy,dz) 

def set_goal_position2():            
    dx=leg_init_pos2[0]
    dy=leg_init_pos2[1]
    dz=leg_init_pos2[2]
    print("dx=",dx,"dy=",dy,"dz=",dz)
    for i in [2,4,6]:
        leg_id=i
        calcul.set_leg_pos_robot_frame(leg_id,dx,dy,dz) 
# ########### Go left ###########    
    # if mt==2: 
    #     if b==0:
    #         print("Boucle 1")
    #         print("Leg_init_pos=",leg_init_pos)
    #         leg_delta=[ dx , dy , -dz]
    #         leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
    #         leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
    #         leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
    #         x=leg_init_pos[0]
    #         z=leg_init_pos[2]
    #         if x==155 :
    #             print("Leg_init_pos=",leg_init_pos)
    #             b=1
    #     if b==1:
    #         b=1
    #         print("Boucle 2")
    #         print("Leg_init_pos=",leg_init_pos)
    #         leg_delta=[ dx , dy , dz]
    #         leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
    #         leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
    #         leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
    #         x=leg_init_pos[0]
    #         z=leg_init_pos[2]
    #         if x==170 and z==90:
    #             print("Leg_init_pos=",leg_init_pos)
    #             b=2
    #     if b==2:
    #         b=2
    #         print("Boucle 3")
    #         print("Leg_init_pos=",leg_init_pos)
    #         leg_delta=[ -3*dx , dy , 0]
    #         leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
    #         leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
    #         leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
    #         x=leg_init_pos[0]
    #         z=leg_init_pos[2]
    #         if x==140 and z==90:
    #             print("Leg_init_pos=",leg_init_pos)
    #             b=0
    #     return b"""########### Go right ###########       
    #     if mt==3:    
    #     if a==0:
    #         print("Boucle 1")
    #         leg_delta=[ dx , dy , -dz]
    #         leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
    #         leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
    #         leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
    #         x=leg_init_pos[0]
    #         z=leg_init_pos[2]
    #         if x==155 :
    #             print("Leg_init_pos=",leg_init_pos)
    #             a=1
    #     if a==1:
    #         a=1
    #         print("Boucle 2")
    #         leg_delta=[ dx , dy , dz]
    #         leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
    #         leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
    #         leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
    #         x=leg_init_pos[0]
    #         z=leg_init_pos[2]
    #         if x==40 and z==90:
    #             print("Leg_init_pos=",leg_init_pos)
    #             a=2
    #     if a==2:
    #         a=2
    #         print("Boucle 3")
    #         leg_delta=[ dx , -2*dy , 0]
    #         leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
    #         leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
    #         leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
    #         x=leg_init_pos[0]
    #         z=leg_init_pos[2]
    #         if x==-40 and z==90:
    #             print("Leg_init_pos=",leg_init_pos)
    #             a=0
    #     return a
    #     if x<=155 and z<=0:
    #         leg_delta=[ x , y , -z ]
    #         leg_final_pos[j]=leg_init_pos[i][j]+(leg_delta[j])
    #     if x<=170 and z<=90:
    #         leg_delta=[ x , y , z ]
    #         leg_final_pos[j]=leg_init_pos[i][j]+(leg_delta[j])
    #     if z>90:
    #         leg_delta=[ -3*x , y , 0 ]
    #         leg_final_pos[j]=leg_init_pos[i][j]+(leg_delta[j])
    #     if x==140 and z<90:
    #         leg_delta=[ x , y , -z ]
    #         leg_final_pos[j]=leg_init_pos[i][j]+(leg_delta[j])