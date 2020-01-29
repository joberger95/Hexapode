import time 
from robot import *
from tkinter import *
import pypot.dynamixel
import numpy

#Initialisation du robot

v=1
mt=0
def forward(event):
    z =event.char 
    mt=0
    x=0
    y=1
    z=2.25
    #robot.next_point(x,y,z,mt)
    calculate_next_point(x,y,z,mt,b_offset=0)
    set_goal_position1()
    calculate_next_point(x,y,z,mt,b_offset=1)
    set_goal_position2()
    print("Go forward")

def back(event):
    s=event.char 
    x=0
    y=-1
    z=-2.25
    mt=1
    calculate_next_point(x,y,z,mt,b_offset=0)
    set_goal_position1()
    calculate_next_point(x,y,z,mt,b_offset=1)
    set_goal_position2()
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
    calculate_next_point(x,y,z,mt)
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

###########interface graphique###############

nmoteur=int(len(found_ids))
nombrepattes=str(npattes)
#Creation de la fenetre
app = Tk()
app.geometry("-600+325")
app.title("Hexapod G1")
com = LabelFrame(app, text="Hexapod G-1", padx=30, pady=30)
com.pack(fill="both", expand="yes")
pattes=Label(com,text="Nombre de pattes : "+nombrepattes,font=(None,20)).pack()
tableau=Listbox(com,height=3)
u=0
for i in range(nmoteur):
    tableau.insert(i,str(found_ids[u]))
    u=u+1
tableau.pack()


#Liste des commandes
textcom =Label(com, text="Z : Avancer\n S : Reculer\n Q : Gauche\n D : Droite\n\n T  : Vitesse +\n G : Vitesse -\n Y : Reset vitesse",font=(None,20)).pack()
com.config(font=("Courier", 70))

#Configuration des bouttons
bouton=Button(app, text="Cercle", command=default)
bouton2=Button(app, text="Défaut", command=default)
bouton3=Button(app, text="Angles", command=anglelimit)
bouton.pack(side= "left",padx=50,pady=5)
bouton2.pack(side= "left",padx=30,pady=5)
bouton3.pack(side= "right",padx=50,pady=5)
bouton.config(font=("Courier", 20))
bouton2.config(font=("Courier", 20))
bouton3.config(font=("Courier", 20))

#Configuration des bind
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