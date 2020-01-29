import time 
#import clav
import robot

def forward():
    mt=0
    x=0
    y=1
    z=2.25
    #robot.next_point(x,y,z,mt)
    robot.calculate_next_point(x,y,z,mt,b_offset=0)
    robot.set_goal_position1()
    robot.calculate_next_point(x,y,z,mt,b_offset=1)
    robot.set_goal_position2()
    print("Go forward")

#robot.init_pos()

while True:
    #clav()
    forward()
    time.sleep(0.01)