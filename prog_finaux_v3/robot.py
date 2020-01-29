import pypot.dynamixel
import numpy 
import calcul 
import time
import kinematics
import math

#Creation des ports et du dxl_io
#Analyse des ports et ouverture de la liaison série
ports=pypot.dynamixel.get_available_ports()
with pypot.dynamixel.DxlIO(ports[0], baudrate=1000000)  as dxl_io :
    print("DXL_IO= ",dxl_io)
    
    #Initialisation a une position initiale
    def init_pos():
        print("Initialisatin des pattes: ")
        for i in [1,2,3,4,5,6]:            
            ids=[i*10+1, i*10+2, i*10+3]
            angles=kinematics.computeIK(i,160,0,90)
            dxl_io.set_goal_position({ids[0]:angles[0] , ids[1]:angles[1] ,ids[2]:angles[2]})
            print("Patte",i,"initialisee")   

  
    a=0
    c=0
    def next_point(ids,dx,dy,dz,mt):
        #Recuperation de la position en x,y,z d'une patte
        x=dxl_io.get_present_position([ids*10+1])
        y=dxl_io.get_present_position([ids*10+2])
        z=dxl_io.get_present_position([ids*10+3])
        x=x[0]
        y=y[0]
        z=z[0]
        kinematics.computeDK(x,y,z)
        global a
        #Ajout de la derivee a la position de la patte
        if mt==0:
            if a==0:
                print("Boucle 1")
                nx=x+dx*math.sin(mt)
                ny=y+dy*math.sin(mt)
                nz=z+dz
                if y>-0.6 and y<0.4 :
                    a=1
                    return a
                if x>154.7 and x<155.3:
                    c=1
                    return c
            if a==1 or c==1:
                ny=y+dy*math.sin(mt)
                nz=z-dz
                print("Boucle 2")
                if y>39.6 and y<40.4:
                    a=2
                    return a
                if x>170.7 and x<171.3:
                    c=2
                    return c
            if a==2:
                ny=y-2*dy
                print("Boucle 3")
                if y>-40.6 and y<-39.8:
                    a=0
                    return a
            if c==2:
                nx=x-2*dx
                if x>139.7 and x<1410.3:
                    c=0
                    return c
            
        #Envoi des nouvelles positions pour le deplacement du robot
        calcul.set_leg_pos_robot_frame(ids,nx,ny,nz)



    ##################################################################

    leg_init_pos=[160,0,90]
    b=0
    def calculate_next_point(dx,dy,dz,mt):   
        ########### Go Forward ########### 
        x=leg_init_pos[0]
        y=leg_init_pos[1]
        z=leg_init_pos[2]
        global b
        if mt==0:  
            if b==0:
                print("Boucle 1")
                leg_delta=[ dx , dy , -dz]
                leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
                leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
                leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
                y=leg_init_pos[1]
                z=leg_init_pos[2]
                if y==0 :
                    print("Leg_init_pos=",leg_init_pos)
                    b=1
            if b==1:
                b=1
                print("Boucle 2")
                leg_delta=[ dx , dy , dz]
                leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
                leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
                leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
                y=leg_init_pos[1]
                z=leg_init_pos[2]
                if y==40 and z==90:
                    print("Leg_init_pos=",leg_init_pos)
                    b=2
            if b==2:
                b=2
                print("Boucle 3")
                leg_delta=[ dx , -2*dy , 0]
                leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
                leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
                leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
                y=leg_init_pos[1]
                z=leg_init_pos[2]
                if y==-40 and z==90:
                    print("Leg_init_pos=",leg_init_pos)
                    b=0
            return b
        ########### Go back ###########  
        if mt==1:    
            if b==0:
                print("Boucle 1")
                leg_delta=[ dx , -dy , -dz]
                leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
                leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
                leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
                y=leg_init_pos[1]
                z=leg_init_pos[2]
                if y==0 :
                    print("Leg_init_pos=",leg_init_pos)
                    b=1
            if b==1:
                b=1
                print("Boucle 2")
                leg_delta=[ dx , -dy , dz]
                leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
                leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
                leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
                y=leg_init_pos[1]
                z=leg_init_pos[2]
                if y==-40 and z==90:
                    print("Leg_init_pos=",leg_init_pos)
                    b=2
            if b==2:
                b=2
                print("Boucle 3")
                leg_delta=[ dx , 2*dy , 0]
                leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
                leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
                leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
                y=leg_init_pos[1]
                z=leg_init_pos[2]
                if y==40 and z==90:
                    print("Leg_init_pos=",leg_init_pos)
                    b=0
            return b

        ########### Go left ###########    
        if mt==2: 
            if b==0:
                print("Boucle 1")
                print("Leg_init_pos=",leg_init_pos)
                leg_delta=[ dx , dy , -dz]
                leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
                leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
                leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
                x=leg_init_pos[0]
                z=leg_init_pos[2]
                if x==155 :
                    print("Leg_init_pos=",leg_init_pos)
                    b=1
            if b==1:
                b=1
                print("Boucle 2")
                print("Leg_init_pos=",leg_init_pos)
                leg_delta=[ dx , dy , dz]
                leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
                leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
                leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
                x=leg_init_pos[0]
                z=leg_init_pos[2]
                if x==170 and z==90:
                    print("Leg_init_pos=",leg_init_pos)
                    b=2
            if b==2:
                b=2
                print("Boucle 3")
                print("Leg_init_pos=",leg_init_pos)
                leg_delta=[ -3*dx , dy , 0]
                leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
                leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
                leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
                x=leg_init_pos[0]
                z=leg_init_pos[2]
                if x==140 and z==90:
                    print("Leg_init_pos=",leg_init_pos)
                    b=0
            return b   

        """########### Go right ###########       
        if mt==3:    
            if a==0:
                print("Boucle 1")
                leg_delta=[ dx , dy , -dz]
                leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
                leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
                leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
                x=leg_init_pos[0]
                z=leg_init_pos[2]
                if x==155 :
                    print("Leg_init_pos=",leg_init_pos)
                    a=1
            if a==1:
                a=1
                print("Boucle 2")
                leg_delta=[ dx , dy , dz]
                leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
                leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
                leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
                x=leg_init_pos[0]
                z=leg_init_pos[2]
                if x==40 and z==90:
                    print("Leg_init_pos=",leg_init_pos)
                    a=2
            if a==2:
                a=2
                print("Boucle 3")
                leg_delta=[ dx , -2*dy , 0]
                leg_init_pos[0]=leg_init_pos[0]+(leg_delta[0])
                leg_init_pos[1]=leg_init_pos[1]+(leg_delta[1])
                leg_init_pos[2]=leg_init_pos[2]+(leg_delta[2])
                x=leg_init_pos[0]
                z=leg_init_pos[2]
                if x==-40 and z==90:
                    print("Leg_init_pos=",leg_init_pos)
                    a=0
            return a
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
        dx=leg_init_pos[0]
        dy=leg_init_pos[1]
        dz=leg_init_pos[2]
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