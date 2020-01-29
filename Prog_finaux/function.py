# -*- coding: utf-8 -*-
import math
import time
import kinematics
import pypot.dynamixel
import numpy

print("Scan...")
ports = pypot.dynamixel.get_available_ports()
dxl_io = pypot.dynamixel.DxlIO(ports[0], baudrate=1000000)
found_ids=dxl_io.scan()
found_ids=found_ids[:-1]
a=len(found_ids)/3
npattes=int(a)
print("Pattes detectées :",npattes)



def set_leg_pos(leg_id,x,y,z):
    id1=leg_id*10+1
    id2=leg_id*10+2
    id3=leg_id*10+3
    angles=kinematics.computeIK(x,y,z)
    dxl_io.set_goal_position({id1:angles[0],id2:angles[1],id3:angles[2]})

def forward():
    #set_leg_pos_robot_frame(1,130,170,0)
    set_leg_pos_robot_frame(6,150,130,70)
    #set_leg_pos_robot_frame(6,175,110,0)
    time.sleep(1)
    #set_leg_pos_robot_frame(1,130,170,30)
    set_leg_pos_robot_frame(6,150,130,0)
    #set_leg_pos_robot_frame(6,175,110,70)
    time.sleep(1)
    #set_leg_pos_robot_frame(1,0,170,30)
    set_leg_pos_robot_frame(6,0,130,0)
    #set_leg_pos_robot_frame(6,175,0,70)
    time.sleep(1)
    #set_leg_pos_robot_frame(1,0,170,0)
    set_leg_pos_robot_frame(6,0,130,70)
    #set_leg_pos_robot_frame(6,175,0,0)
    time.sleep(1)

def anglelimit():
    b=0
    for i in range (npattes):
        dxl_io.set_angle_limit({found_ids[b]:(-107,107)})
        dxl_io.set_angle_limit({found_ids[b+1]:(-107,107)})
        dxl_io.set_angle_limit({found_ids[b+2]:(-138,91)})
        b=b+3

def default_pos():
    b=0
    for i in range (npattes):
        dxl_io.set_goal_position({found_ids[b]:0,found_ids[b+1]:45,found_ids[b+2]:-60})
        b=b+3


def set_leg_pos_robot_frame(leg_id,x,y,z):
    if leg_id==1:
        nx=x*math.cos(math.pi/4)-y*math.sin(math.pi/4)
        ny=y*math.cos(math.pi/4)+x*math.sin(math.pi/4)
        nz=z
    if leg_id==2:
        nx=x*math.cos(math.pi/4)-y*math.sin(math.pi/4)
        ny=y*math.cos(math.pi/4)+x*math.sin(math.pi/4)
        nz=z 
    if leg_id==3:
        nx=-y
        ny=x
        nz=z
    if leg_id==4:
        nx=x*math.cos(-math.pi/4)-y*math.sin(-math.pi/4)
        ny=y*math.cos(-math.pi/4)+x*math.sin(-math.pi/4)
        nz=z
    if leg_id==5:
        nx=x*math.cos(5*math.pi/4)-y*math.sin(5*math.pi/4)
        ny=y*math.cos(5*math.pi/4)+x*math.sin(5*math.pi/4)
        nz=z
    if leg_id==6:
        nx=x
        ny=-y
        nz=z
    set_leg_pos(leg_id,nx,ny,nz)


def circle(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y


def circle_demo(period, r):
    t0 = time.time()
    ports = pypot.dynamixel.get_available_ports()
    dxl_io = pypot.dynamixel.DxlIO(ports[0], baudrate=1000000)
    while True:
        t = time.time() - t0
        theta = 2 * math.pi * t / period
        z = 0
        x, y = circle(r, theta)
        x = x + 200
        # Il suffit d'envoyer ça à l'IK
        angles = kinematics.computeIK(x, y, z)
        dxl_io.set_goal_position({41: angles[0], 42: angles[1], 43: angles[2]})
        time.sleep(0.05)
        


if __name__ == "__main__":
    #print("defaut")
    #default_pos()
    anglelimit()
    