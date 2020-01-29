import time 
import clav
import robot

robot.init_pos()
time.sleep(1)

while True:
    clav()
    time.sleep(0.2)     