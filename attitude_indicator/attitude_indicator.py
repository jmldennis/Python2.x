from Tkinter import *
from math import *
#from time import *

#Global varibles
width = 1024
height = 768
att_elev_vel = 0
att_rot_vel = 0
att_rot_deg = 0
rad = 400
spacing = 40
att_pos_xy = [width/2,height/2] 
att_pos_cir = [width/2-rad,height/2,width/2+rad,height/2]
fps = 1000/60 

# Draws the static background of the attitude indicator
def draw_background():
    global frame

    #Attitude Background Sky/Ground/Center Line
    frame.create_rectangle(0, 0, width, height/2, fill="blue")
    frame.create_rectangle(0,height/2,width,height,fill="brown")
    frame.create_line(0, height/2, width, height/2,fill="White")

    #Attitude Background Elevation Lines Above
    frame.create_line(width/2-25, height/2-spacing, width/2+25, height/2-spacing,fill="White")
    frame.create_line(width/2-50, height/2-spacing*2, width/2+50, height/2-spacing*2,fill="White")
    frame.create_line(width/2-25, height/2-spacing*3, width/2+25, height/2-spacing*3,fill="White")
    frame.create_line(width/2-125, height/2-spacing*4, width/2+125, height/2-spacing*4,fill="White")
    frame.create_line(width/2-25, height/2-spacing*5, width/2+25, height/2-spacing*5,fill="White")
    frame.create_line(width/2-50, height/2-spacing*6, width/2+50, height/2-spacing*6,fill="White")
    frame.create_line(width/2-25, height/2-spacing*7, width/2+25, height/2-spacing*7,fill="White")
    frame.create_line(width/2-125, height/2-spacing*8, width/2+125, height/2-spacing*8,fill="White")
    frame.create_line(width/2-25, height/2-spacing*9, width/2+25, height/2-spacing*9,fill="White")

    #Attitude Background Elevation Lines Below
    frame.create_line(width/2-25, height/2+spacing, width/2+25, height/2+spacing,fill="White")
    frame.create_line(width/2-50, height/2+spacing*2, width/2+50, height/2+spacing*2,fill="White")
    frame.create_line(width/2-25, height/2+spacing*3, width/2+25, height/2+spacing*3,fill="White")
    frame.create_line(width/2-125, height/2+spacing*4, width/2+125, height/2+spacing*4,fill="White")
    frame.create_line(width/2-25, height/2+spacing*5, width/2+25, height/2+spacing*5,fill="White")
    frame.create_line(width/2-50, height/2+spacing*6, width/2+50, height/2+spacing*6,fill="White")
    frame.create_line(width/2-25, height/2+spacing*7, width/2+25, height/2+spacing*7,fill="White")
    frame.create_line(width/2-125, height/2+spacing*8, width/2+125, height/2+spacing*8,fill="White")
    frame.create_line(width/2-25, height/2+spacing*9, width/2+25, height/2+spacing*9,fill="White")

    #Attitude Degree Numbers Above
    frame.create_text(width/2-150, height/2-spacing*4,text="10",fill="White")
    frame.create_text(width/2+150, height/2-spacing*4,text="10",fill="White")
    frame.create_text(width/2-150, height/2-spacing*8,text="20",fill="White")
    frame.create_text(width/2+150, height/2-spacing*8,text="20",fill="White")

    #Attitude Degree Numbers Below
    frame.create_text(width/2-150, height/2+spacing*4,text="10",fill="White")
    frame.create_text(width/2+150, height/2+spacing*4,text="10",fill="White")
    frame.create_text(width/2-150, height/2+spacing*8,text="20",fill="White")
    frame.create_text(width/2+150, height/2+spacing*8,text="20",fill="White")
    

#Updates the moving attitude indicator
def draw_attitude():
    global frame
    global attitude1
    global att_pos_cir

    #attitude1 = frame.create_line(att_pos_cir[0],att_pos_cir[1],att_pos_cir[2],att_pos_cir[3],fill="white",width=10)
    frame.coords(attitude1, att_pos_cir[0],att_pos_cir[1],att_pos_cir[2],att_pos_cir[3])

#Start movement when key is pressed.  Velocity is set, movement is based on fps (60*1=60 pixels per second)
def key_press(key):
    global frame
    global att_pos_xy
    global att_rot_deg
    global rad
    global att_rot_vel
    global att_elev_vel

    #Start Movement based on Keydown
    if (key.char == "a"):
        att_rot_vel = -1
    if (key.char == "d"):
        att_rot_vel = 1
    if (key.char == "w"):
        att_elev_vel = -1
    if (key.char == "s"):
        att_elev_vel = 1


#Stop movement when key is released
def key_release(key):
    global att_rot_vel
    global att_elev_vel

    #Stop movement velocity based on keyup
    if (key.char == "a"):
        att_rot_vel = 0
    if (key.char == "d"):
        att_rot_vel = 0
    if (key.char == "w"):
        att_elev_vel = 0
    if (key.char == "s"):
        att_elev_vel = 0


#Timer 
def tick():
    global frame
    global att_rot_vel
    global att_elev_vel
    global att_pos_cir
    global att_pos_xy
    global att_rot_deg

    #Update position based on movement velocity from key press
    att_pos_xy[1] = att_pos_xy[1] + att_elev_vel
    att_rot_deg = att_rot_deg + att_rot_vel
 

    #Update position
    att_pos_cir[0] = att_pos_xy[0]-rad*cos(radians(att_rot_deg))
    att_pos_cir[1] = att_pos_xy[1]-rad*sin(radians(att_rot_deg))
    att_pos_cir[2] = att_pos_xy[0]+rad*cos(radians(att_rot_deg))
    att_pos_cir[3] = att_pos_xy[1]+rad*sin(radians(att_rot_deg))

    #Draws moving attitude
    draw_attitude()

    #Continue Timer Loop
    frame.after(fps,tick)


#Setup Tkinter
root = Tk()
root.title("Attitude Indicator")

#Create frame widthxheight
frame = Canvas(root, width=width, height=height)
frame.pack()

 # Draws the static background of the attitude indicator
draw_background()

#Initialize Attitude Indicator to be called by draw_attitute in tick definition
attitude1 = frame.create_line(att_pos_cir[0],att_pos_cir[1],att_pos_cir[2],att_pos_cir[3],fill="white",width=10)

#Detect Key Presses
frame.bind("<KeyPress>",key_press)
frame.bind("<KeyRelease>",key_release)

#Start timer and movement.  Runs movement at fps (60).
frame.after(fps,tick)

#set focus for keyboard input
frame.focus_set()

#Mainloop
mainloop()
