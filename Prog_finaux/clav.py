import tkinter as tk
import math
 
def forward(event):
    z =event.char 
    meta_theta=0
    print("Go foward")
    return meta_theta
def back(event):
    s=event.char 
    meta_theta=math.radians(180)
    print("Go back")
    return meta_theta
def left(event):
    q=event.char 
    meta_theta=math.radians(-90)
    print("Go left")
    return meta_theta
def right(event):
    d=event.char
    meta_theta=math.radians(90)
    print("Go right")
    return meta_theta

app=tk.Tk()
app.bind("<z>", forward)
app.bind("<s>", back)
app.bind("<q>", left)
app.bind("<d>", right)
app.mainloop()

def event(event):
    if 'z'==event.char:
        