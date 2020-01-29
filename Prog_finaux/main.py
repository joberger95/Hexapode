# -*- coding: utf-8 -*-
#import legmoves 
import calculs
import time
import Initrobot


if __name__ == "__main__":
    print("Donner une direction au robot")
    #calculs.default_pos()

    i=160
    j=-80
    k=90
    a=0
    while True:   
        t=2   
        if a==0:
            calculs.set_leg_pos_robot_frame(t,i,j,k)
            j+=1
            k=k-1.125
            if j==0 and k==0:
                a=1

        if a==1:
            calculs.set_leg_pos_robot_frame(t,i,j,k)
            i=160
            j+=1
            k=k+1.125
            if j==80 and k==90:
                a=2
                
        if a==2:
            calculs.set_leg_pos_robot_frame(t,i,j,k)
            i=160
            j-=5
            if j==-80 and k==90:
                a=0    
        time.sleep(0.005)