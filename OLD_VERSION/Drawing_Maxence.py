#!/usr/bin/python2.7
import math
import itertools
import time
import numpy
import pypot.dynamixel
import sys

a=0
b=0
c=0

def leg_dk(theta1,theta2,theta3,l1,l2,l3):
	x1=(l1*math.cos(theta1))
	y1=(l1*math.sin(theta1))
	z1=0
	d_12=l2*math.cos(theta2)
	x2=((l1+d_12)*math.cos(theta1))
	y2=((l1+d_12)*math.sin(theta1))
	z2=z1+l2*math.sin(theta2)
	d_23=(l3*math.cos(theta2+theta3))
	x3=((l1+d_12+d_23)*math.cos(theta1))
	y3=((l1+d_12+d_23)*math.sin(theta1))
	z3=(z2+l3*math.sin(theta2+theta3))
	print ("P3 : x={0}, y={1}, z={2}".format(x3,y3,z3))
	return x3,y3,-z3

def axis_correction(theta1,theta2,theta3):
	theta2c=-14
	theta3c=theta2c-47
	theta2=theta2-theta2c
	theta3=-(theta3-theta3c)
	print ("Theta1 = {0}, Theta2 = {1}, Theta3 = {2}".format(a,b,c))
	print("\n")
#Il faut passer les angles en radians
	theta1=theta1*math.pi/180
	theta2=theta2*math.pi/180
	theta3=theta3*math.pi/180
	return theta1, theta2, theta3

def angles(l,m,n):
	angles=dxl_io.get_present_position([61,62,63])
	a=angles[0]
	b=angles[1]
	c=angles[2]
	print ("Position moteur 1 : {0}, position moteur 2 : {1}, position moteur 3 : {2}".format(a,b,c))
	print("\n")
	a,b,c=axis_correction(a,b,c)

	return a,b,c

if __name__ == '__main__':
	with pypot.dynamixel.DxlIO('/dev/ttyACM1', baudrate=1000000) as dxl_io:
		dxl_io.disable_torque([61,62,63])
		while True:
			a,b,c=angles(a,b,c)
			x,y,z=leg_dk(a,b,c,54.8,67,132)
			time.sleep(2.0)  # we wait for 2s
		

