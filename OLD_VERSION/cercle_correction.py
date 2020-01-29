# -*- coding: utf-8 -*-
import math
import time
import kinematics
import pypot.dynamixel


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
    circle_demo(5, 30)

