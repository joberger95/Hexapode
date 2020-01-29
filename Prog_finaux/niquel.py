import time
import pypot.dynamixel
import numpy  
import kinematics
import math
import tkinter as tk
import tkinter.messagebox as tkm

#Initialisation du robot
print("****************************\n")
print("          Scan...\n")
print("****************************\n")

ports = pypot.dynamixel.get_available_ports()
dxl_io = pypot.dynamixel.DxlIO(ports[0], baudrate=1000000)
found_ids=dxl_io.scan()
found_ids=found_ids[:-1]
npattes=int(len(found_ids)/3)
print("Pattes detectées :",npattes)

def set_leg_pos_robot_frame(leg_id,x,y,z,meta_theta=0):
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

def anglelimit():
    b=0
    for i in range (npattes):
        dxl_io.set_angle_limit({found_ids[b]:(-107,107)})
        dxl_io.set_angle_limit({found_ids[b+1]:(-107,107)})
        dxl_io.set_angle_limit({found_ids[b+2]:(-138,91)})
        b=b+3

def default_pos():
    for i in [1,2,3,4,5,6]:
            angles=kinematics.computeIK(i,180,0,90)
            print("Initialisatin des pattes: ")
            ids=[i*10+1, i*10+2, i*10+3]
            dxl_io.set_goal_position({ids[0]:angles[0] , ids[1]:angles[1] ,ids[2]:angles[2]})
            print("Patte",i,"initialisee")

def forward():
        i=160
        j=-40
        k=90
        o=0
        p=0
        a=0
        val=0
        while val==0:  
            for t in [1,3,5]: 
                if a==0:
                    set_leg_pos_robot_frame(t,i,j,k)
                    j+=1
                    k=k-2.25
                    if j==0 and k==0:
                        a=1
                        
                if a==1:
                    set_leg_pos_robot_frame(t,i,j,k)
                    i=160
                    j+=1
                    k=k+2.25
                    if j==40 and k==90:
                        a=2
                        for t in [2,4,6]:
                            set_leg_pos_robot_frame(t,160,0,80)                        
                if a==2:
                    set_leg_pos_robot_frame(t,i,j,k)
                    i=160
                    j-=2
                    if j==-40 and k==90:
                        a=0 
                        val=1
                    
            time.sleep(0.04)

        while val==1:  
            for t in [2,4,6]: 
                if a==0:
                    set_leg_pos_robot_frame(t,i,j,k)
                    j+=1
                    k=k-2.25
                    if j==0 and k==0:
                        a=1
                        
                if a==1:
                    set_leg_pos_robot_frame(t,i,j,k)
                    i=160
                    j+=1
                    k=k+2.25
                    if j==40 and k==90:
                        a=2
                        for t in [1,3,6]:
                            set_leg_pos_robot_frame(t,160,0,80)                        
                if a==2:
                    set_leg_pos_robot_frame(t,i,j,k)
                    i=160
                    j-=2
                    if j==-40 and k==90:
                        a=0 
                        val=0
                    
            time.sleep(0.04)

def commandforward(event):
    z =event.char
    print("Go forward")
    forward()
def commandback(event):
    s=event.char 
    print("Go back")
    set_leg_pos_robot_frame(2,180,20,60)
def commandleft(event):
    q=event.char 
    print("Go left")
def commandright(event):
    d=event.char
    print("Go right")
"""def commandcircle(event):
    e=event.char
    print("Circle")
    circle_demo(5,45)"""
def commanddefault(event):
    d=event.char
    print("Position par defaut")
    default_pos()

#interface graphique
def callback():
    if tkm.askyesno('Hexapod G-1', 'Souhaitez vous définir les angles limites ?'):
        anglelimit()
        print('Les angles limites ont été défini')
    else:
        print('angles limites non défini')
callback()
app = tk.Tk()
l = tk.LabelFrame(app, text="Hexapod G-1", padx=50, pady=50)
l.pack(fill="both", expand="yes")
tk.Label(l, text="Z : Avancer\n S : Reculer\n Q : Gauche\n D : Droite").pack()
#bouton=tk.Button(app, text="Cercle", command=circle_demo)
bouton2=tk.Button(app, text="Défaut", command=default_pos)
#bouton.pack()
bouton2.pack()

app.bind("<z>", commandforward)
app.bind("<s>", commandback)
app.bind("<q>", commandleft)
app.bind("<d>", commandright)
#app.bind("<a>", commandcircle)
app.bind("<f>", commanddefault)
app.mainloop()