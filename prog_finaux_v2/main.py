import robot
import time 
import clav

t0=time.time()
r=robot()
while True:
    clav()
    robot.t=time.time()-t0
    #robot.calculate_next_point()
    #robot.set_goal_position()
    time.sleep(0.02) 
    