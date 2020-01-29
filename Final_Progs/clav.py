import tkinter as tk
import robot

v=1
mt=0
def forward(event):
    z =event.char 
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

def back(event):
    s=event.char 
    x=0
    y=-1
    z=-2.25
    mt=1
    robot.calculate_next_point(x,y,z,mt,b_offset=0)
    robot.set_goal_position1()
    robot.calculate_next_point(x,y,z,mt,b_offset=1)
    robot.set_goal_position2()
    print("Go back")

def left(event):
    q=event.char 
    x=1
    y=0
    z=6
    mt=2
    #robot.calculate_next_point(x,y,z,mt)
    #robot.set_goal_position()
    print("Go left")

def right(event):
    d=event.char
    x=1
    y=0
    z=6
    mt=3  
    robot.calculate_next_point(x,y,z,mt)
    #robot.set_goal_position()
    print("Go right")

def up_meta_theta(event):
    e=event.char
    global mt
    mt += 1
    print("Angle de direction= ",mt,"°")

def down_meta_theta(event):
    a=event.char
    global mt
    mt -= 1
    print("Angle de direction= ",mt,"°")

def reset_meta_theta(event):
    r=event.char
    global mt 
    mt=0
    print("Angle de direction= ",mt,"°")

def up_vitesse(event):
    t=event.char
    global v
    v += 0.1
    print("Coefficient de vitesse=",v)

def down_vitesse(event):
    g=event.char
    global v
    v-=0.1
    print("Coefficient de vitesse=",v)

def reset_vitesse(event):
    y=event.char
    global v
    v=0
    print("Coefficient de vitesse=",v)

app=tk.Tk()
app.bind("<z>", forward)
app.bind("<s>", back)
app.bind("<q>", left)
app.bind("<d>", right)
app.bind("<e>", up_meta_theta)
app.bind("<a>", down_meta_theta)
app.bind("<r>", reset_meta_theta)
app.bind("<t>", up_vitesse)
app.bind("<g>", down_vitesse)
app.bind("<y>", reset_vitesse)
app.mainloop()