# -*- coding: utf-8 -*-
import math
import time
import pypot.dynamixel
import numpy
import kinematics
import Initrobot

def set_leg_pos_robot_frame(leg_id,x,y,z):
    #patte 1
    if leg_id==1:
        nx=x*math.cos(7*math.pi/4)-y*math.sin(7*math.pi/4)
        ny=-y*math.cos(7*math.pi/4)+x*math.sin(7*math.pi/4)
        nz=z
    #patte 2
    if leg_id==2:
        nx=x*math.cos(math.pi/4)-y*math.sin(math.pi/4)
        ny=y*math.cos(math.pi/4)+x*math.sin(math.pi/4)
        nz=z 
    #patte 3
    if leg_id==3:
        nx=x*math.cos(math.pi/4)-y*math.sin(math.pi/4)
        ny=-y*math.cos(math.pi/4)-x*math.sin(math.pi/4)
        nz=z
    #patte 4
    if leg_id==4:
        nx=x*math.cos(3*math.pi/4)-y*math.sin(3*math.pi/4)
        ny=y*math.cos(3*math.pi/4)+x*math.sin(3*math.pi/4)
        nz=z   
    #patte5
    if leg_id==5:
        nx=x*math.cos(math.pi/4)-y*math.sin(math.pi/4)
        ny=-y*math.cos(math.pi/4)-x*math.sin(math.pi/4)
        nz=z 
    #patte 6
    if leg_id==6:
        nx=x
        ny=-y
        nz=z
    set_leg_pos(leg_id,nx,ny,nz)

def set_leg_pos(leg_id,x,y,z):
    id1=leg_id*10+1
    id2=leg_id*10+2
    id3=leg_id*10+3
    angles=kinematics.computeIK(x,y,z)  
    Initrobot.dxl_io.set_goal_position({id1:angles[0],id2:angles[1],id3:angles[2]})

"""def circle(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y"""


"""def circle_demo(period, r):
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
        time.sleep(0.05)"""
