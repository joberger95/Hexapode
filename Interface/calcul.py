import math
import pypot.dynamixel
import robot
import kinematics

def set_leg_pos_robot_frame(leg_id,x,y,z):
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
    ids=[leg_id*10+1, leg_id*10+2, leg_id*10+3]
    angles=kinematics.computeIK(leg_id,x,y,z)  
    
    robot.dxl_io.set_goal_position({ids[0]:angles[0],ids[1]:angles[1],ids[2]:angles[2]})