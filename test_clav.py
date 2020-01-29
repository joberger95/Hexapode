import tkinter as tk
 
def forward(event):
    z =event.char
    print("Go forward")
def back(event):
    s=event.char 
    print("Go back")
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