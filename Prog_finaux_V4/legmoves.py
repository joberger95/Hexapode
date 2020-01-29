import pypot.dynamixel
import numpy 
import time
import calculs
import tkinter as tk
 
def forward(event):
    z =event.char
    print("Go forward")
    calculs.set_leg_pos_robot_frame(2,180,0,90)
def back(event):
    s=event.char 
    print("Go back")
    calculs.set_leg_pos_robot_frame(2,180,20,60)
def left(event):
    q=event.char 
    print("Go left")
def right(event):
    d=event.char
    print("Go right")

app = tk.Tk()
app.bind("<z>", forward)
app.bind("<s>", back)
app.bind("<q>", left)
app.bind("<d>", right)
app.mainloop()