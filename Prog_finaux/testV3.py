
import time
import pypot.dynamixel
import numpy  
import kinematics
import math
#import clav

def set_leg_pos_robot_frame(leg_id,x,y,z,meta_theta=0):
    #patte 1 OK
    if leg_id==1:
        nx=x*math.cos(math.pi/4-math.pi/2)-y*math.sin(math.pi/4-math.pi/2)
        ny=-y*math.cos(math.pi/4-math.pi/2)-x*math.sin(math.pi/4-math.pi/2)
        nz=z
    #patte 2 OK 
    if leg_id==2:
        nx=x*math.cos(7*math.pi/4)-y*math.sin(7*math.pi/4)
        ny=y*math.cos(7*math.pi/4)+x*math.sin(7*math.pi/4)
        nz=z
    #patte 3 OK
    if leg_id==3:
        nx=x
        
        ny=y
        nz=z
    #patte 4  OK
    if leg_id==4:
        nx=x*math.cos(math.pi/4)-y*math.sin(math.pi/4)
        ny=y*math.cos(math.pi/4)+x*math.sin(math.pi/4)
        nz=z 
    #patte 5 OK
    if leg_id==5:
        nx=x*math.cos(math.pi/4)-y*math.sin(math.pi/4)
        ny=-y*math.cos(math.pi/4)-x*math.sin(math.pi/4)
        nz=z 
    #patte 6 OK
    if leg_id==6:
        nx=x
        ny=-y
        nz=z  
    set_leg_pos(leg_id,nx,ny,nz)

def set_leg_pos(leg_id,x,y,z):
    id1=leg_id*10+1
    id2=leg_id*10+2
    id3=leg_id*10+3
    angles=kinematics.computeIK(leg_id,x,y,z)  
    dxl_io.set_goal_position({id1:angles[0],id2:angles[1],id3:angles[2]})

#Constantes de trajectoire des pattes
i=160
j=-40
k=90
o=0
p=0
a=0
#mt=clav.meta_theta 
#print("meta_theta= ",mt)
ports=pypot.dynamixel.get_available_ports()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
with pypot.dynamixel.DxlIO(ports[0], baudrate=1000000)  as dxl_io :
    while True:
        for t in [1,3,5]: 
            if a==0:
                set_leg_pos_robot_frame(t,i,j,k)
                j+=1
                k=k-2.25
                if j==0 and k==0:
                    a=1
                    
            if a==1:
                set_leg_pos_robot_frame(t,i,j,k)
                j+=1
                k=k+2.25
                if j==40 and k==90:
                    a=2                   
            if a==2:
                set_leg_pos_robot_frame(t,i,j,k)
                j-=2
                if j==-40 and k==90:
                    a=0 
        """"""""""""""""""""""""""""""""""""""""""""""""""        
        for t in [2,4,6]: 
            if a==0:
                set_leg_pos_robot_frame(t,i,o,p)
                o+=1
                p+=2.25
                if o==40 and p==90:
                    a=1   
            if a==1:
                set_leg_pos_robot_frame(t,i,o,p)
                o-=5
                if o==-40:
                    a=2                   
            if a==2:
                set_leg_pos_robot_frame(t,i,o,p)
                o+=1
                p-=2.25
                if j==0 and p==0:
                    a=0 
        time.sleep(0.1)
