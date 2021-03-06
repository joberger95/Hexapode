import math
import robot
import kinematics

def leg_move_delta(leg_id,dx,dy,dz):
    init=robot.leg_init_pos[leg_id-1]
    rx=dx+init[0]
    ry=dy+init[1]
    rz=dz+init[2]
    set_leg_pos_robot_frame(leg_id,rx,ry,rz)

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
    id1=leg_id*10+1
    id2=leg_id*10+2
    id3=leg_id*10+3
    angles=kinematics.computeIK(leg_id,x,y,z)  
    dxl_io.set_goal_position({id1:angles[0],id2:angles[1],id3:angles[2]})


