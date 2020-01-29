import tkinter as tk
import robot
 
def forward(event):
    z =event.char 
    x=0
    y=1
    z=2.25
    robot.calculate_next_point(x,y,z)
    print("Go forward")

def back(event):
    s=event.char 
    x=0
    y=-1
    z=-2.25
    robot.calculate_next_point(x,y,z)
    print("Go back")

def left(event):
    q=event.char 
    x=1
    y=1
    z=2.25
    robot.calculate_next_point(x,y,z)
    print("Go left")

def right(event):
    d=event.char
    x=-1
    y=-1
    z=-2.25    
    robot.calculate_next_point(x,y,z)
    print("Go right")

app=tk.Tk()
app.bind("<z>", forward)
app.bind("<s>", back)
app.bind("<q>", left)
app.bind("<d>", right)
app.mainloop()