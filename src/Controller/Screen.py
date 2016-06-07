#!/usr/bin/python
from Tkinter import *
import tkFont
#import tkMessageBox #voor pop-up
import os
from time import sleep
import time
import Joy
#import Gyro
import threading
from PIL import ImageTk, Image
import spidercommunication
#import Spin_battery
#import Controller_battery
#gyroscope
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom
win=Tk()
myFont = tkFont.Font(family = 'Helvetica',size = 12, weight = 'bold')
win.title("Black Widow")
win.geometry("550x320")
app = FullScreenApp(win)
# app = Frame(win)
# app.grid()
path = "/home/pi/Documents/Controller/Black-widow.jpeg"
path0 = "/home/pi/Documents/Controller/battery-0.png"
path1 = "/home/pi/Documents/Controller/battery-1.png"
path2 = "/home/pi/Documents/Controller/battery-2.png"
path3 = "/home/pi/Documents/Controller/battery-3.png"
path4 = "/home/pi/Documents/Controller/battery-4.png"
img = ImageTk.PhotoImage(Image.open(path))
battery_0 = ImageTk.PhotoImage(Image.open(path0))
battery_1 = ImageTk.PhotoImage(Image.open(path1))
battery_2 = ImageTk.PhotoImage(Image.open(path2))
battery_3 = ImageTk.PhotoImage(Image.open(path3))
battery_4 = ImageTk.PhotoImage(Image.open(path4))
bt_spider = spidercommunication.SpiderCommunication("00:1A:7D:DA:71:06",1)
running = 1
lastrunning = 1
delay = 50
active="green"
inactive="red"
active1 = "yellow"
dans = False
batterijsample=0
aanval = False
prik = False
bt = False
dansstate = "disabled"
aanvalstate = "disabled"
gyroThread = threading.Thread(target=bt_spider.synchronizeFrontLegs)

def active_background():
    mode_1_button["activebackground"] = mode_1_button["bg"]
    mode_2_button["activebackground"] = mode_2_button["bg"]
    mode_3_button["activebackground"] = mode_3_button["bg"]
    mode_4_button["activebackground"] = mode_4_button["bg"]
    mode_5_button["activebackground"] = mode_5_button["bg"]
    mode_6_button["activebackground"] = mode_6_button["bg"]
    dansmode1_button["activebackground"] = dansmode1_button["bg"]
    prik_button["activebackground"] = prik_button["bg"]

def imgselect(bier):
    if(bier==1):
        batterijsample=2#Spin_battery.read()
    if(bier==2):
        batterijsample=3#Controller_battery.read()
    if(batterijsample==1):
        return battery_1
    if(batterijsample==2):
        return battery_2
    if(batterijsample==3):
        return battery_3
    if(batterijsample==4):
        return battery_4
    else:
        return battery_0

def main_loop():
    global batterij_foto
    global t
    if(running==1):
        print uitvoer_1()
    if(running==2):
        print uitvoer_2()
    if(running==3):
        print uitvoer_3()
    if(running==4):
        print uitvoer_4()
    if(running==5):
        print uitvoer_5()
    if(running==6):
        print uitvoer_6()
    win.after(delay,main_loop)
    batterij_foto["image"] = imgselect(1)
    batterij_controller["image"] = imgselect(2)

def mode_1(): #Voortbewegen (default)
    global lastrunning
    global running
    global delay
    lastrunning=running
    running=1
    delay=1000
    #get x and y location of joystick
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    print "MOVEE"
    bt_spider.move(20,20)
    buttons[lastrunning]["bg"]=inactive
    buttons[running]["bg"]=active
    active_background()
    reset_knoppen()

def mode_2(): #Dansmode
    global lastrunning
    global running
    global delay
    lastrunning=running
    running=2
    delay=1000
    buttons[lastrunning]["bg"]=inactive
    buttons[running]["bg"]=active
    active_background()
    reset_knoppen()

def mode_3(): #Aanvalmode
    global lastrunning
    global running
    global delay
    global prik
    global aanval
    global gyroThread
    lastrunning=running
    running=3
    delay=1000
    if not aanval:
        aanval = True
        gyroThread = threading.Thread(target=bt_spider.synchronizeFrontLegs)
        gyroThread.start()
    else:
        aanval = False
        bt_spider.synclegs = False
        gyroThread.join()
    buttons[lastrunning]["bg"]=inactive
    buttons[running]["bg"]=active
    prik_button["bg"]=inactive
    prik=False
    active_background()
    reset_knoppen()

def mode_4():#Automatisch Lijn mode
    global lastrunning
    global running
    global delay
    lastrunning=running
    running=4
    delay=1000
    bt_spider.autonomousLine()
    buttons[lastrunning]["bg"]=inactive
    buttons[running]["bg"]=active
    active_background()
    reset_knoppen()

def mode_5():#Automatisch ballon mode
    global lastrunning
    global running
    global delay
    lastrunning=running
    running=5
    delay=1000
    bt_spider.autonomousBalloon()
    buttons[lastrunning]["bg"]=inactive
    buttons[running]["bg"]=active
    active_background()
    reset_knoppen()

def mode_6(): #Draagmode
    global lastrunning
    global running
    global delay

    lastrunning=running
    running=6
    delay=1000
    bt_spider.goToSleep()
    buttons[lastrunning]["bg"]=inactive
    buttons[running]["bg"]=active
    active_background()
    reset_knoppen()

def start_stop_dans():
    global dans
    if not dans:
        dans = True
        dansmode1_button["bg"]=active
        bt_spider.dance(1)
        dansmode1_button["text"]="Stop"
        active_background()
    else:
        dans = False
        dansmode1_button["bg"]=inactive
        bt_spider.dance(0)
        dansmode1_button["text"]="Start"
        active_background()

def prik_uitvoer():
    global prik
    if prik:
        prik = False
        prik_button["bg"]=inactive
    else:
        prik = True
        bt_spider.stab()
        prik_button["bg"]=active
    active_background()

def exitProgram():
    print "Exit Button Pressed"
    win.quit()

def uitvoer_1():
    return "joystickpos"
    #return running,Joy.read_x(),Joy.read_y()

def uitvoer_2():
    return running,dans

def uitvoer_3():
    return running,'''Gyro.x_gyroscoop()'''"100",prik

def uitvoer_4():
    return running

def uitvoer_5():
    return running

def uitvoer_6():
    return running

def reset_knoppen():
    global dans
    global prik
    global dansstate
    global aanvalstate
    if (lastrunning==2) & (running!=2):
        dansstate = "disabled"
        dansmode1_button["state"]= dansstate
        dansmode1_button["bg"]=inactive
        dans = 0
    if (lastrunning==3) & (running!=3):
        aanvalstate = "disabled"
        prik_button["state"]=aanvalstate
        prik_button["bg"]=inactive
        prik = False
    if (running==2) & (lastrunning!=2):
        dansstate = "normal"
        dansmode1_button["state"]= dansstate
        aanvalstate = "disabled"
        prik_button["state"]=aanvalstate
        prik_button["bg"]=inactive
        prik = False
    if (running==3) & (lastrunning!=3):
        dansstate = "disabled"
        dansmode1_button["state"]= dansstate
        dansmode1_button["bg"]=inactive
        aanvalstate = "normal"
        prik_button["state"]=aanvalstate
    if (running==2) & (lastrunning==2):
        dansmode1_button["state"]= dansstate
        dansmode1_button["bg"]=inactive
        dans = 0
        active_background()

def bt_knop():
    global bt
    try:
        if not bt:
            bt_spider.start()
            bt = True
            bt_connect["bg"]=active
        else:
            bt_spider.shutdown()
            bt = False
            bt_connect["bg"]=inactive
        #succesvol
    except ServerDown as e:
        print e.value
        #doe iets als bluetooth niet wil verbinden

var =StringVar()

#Beschrijving Knoppen
mode_1_button = Button(win, text = "Lopen", font = myFont, command = mode_1, height=2, width=6, bg = "red")
mode_2_button = Button(win, text = "Dansen", font = myFont, command = mode_2, height=2, width=6, bg = "red")
mode_3_button = Button(win, text = "Aanvallen", font = myFont, command = mode_3, height=2, width=6, bg = "red")
mode_4_button = Button(win, text = "Lijn", font = myFont, command = mode_4, height=2, width=6, bg = "red")
mode_5_button = Button(win, text = "Ballon", font = myFont, command = mode_5, height=2, width=6, bg = "red")
mode_6_button = Button(win, text = "Draag", font = myFont, command = mode_6, height=2, width=6, bg = "red")
bt_connect = Button(win, text = "BT Connect", font = myFont, command = bt_knop, height =2,width=6, bg = "red")

buttons=[0,mode_1_button,mode_2_button,mode_3_button,mode_4_button,mode_5_button,mode_6_button]

dansmode1_button = Button(win, text = "Start", font = myFont, command = start_stop_dans, height=2, width=6, bg = "red", state = dansstate)
prik_button = Button(win, text = "Prik", font = myFont, command = prik_uitvoer, height=2, width=6, bg = "red", state = aanvalstate)

controller_text = Label(win,text="Controller")
spin_text = Label(win,text="Spin")

foto = Label(win, image = img)
batterij_controller = Label(win, image = imgselect(2))
batterij_var = Label(win, textvariable=var)
batterij_foto = Label(win, image = imgselect(1))


mode_1_button.grid(row=0,column=0)
mode_2_button.grid(row=0,column=1)
mode_3_button.grid(row=0,column=2)
mode_4_button.grid(row=0,column=3)
mode_5_button.grid(row=0,column=4)
mode_6_button.grid(row=0,column=5)
dansmode1_button.grid(row=1,column=0, pady=15, rowspan=3)
bt_connect.grid(row=1,column=4)
prik_button.grid(row=1,column=3, pady=15, rowspan=3)
foto.grid(row=5,column=0,columnspan=10)
batterij_foto.grid(row=1,column=6, rowspan=2)
batterij_controller.grid(row=1,column=5, rowspan=2)
controller_text.grid(row=3,column=4)
spin_text.grid(row=3,column=5)

active_background()
#mode_1()
main_loop()

'''
#Poisite knoppen
mode_1_button.pack(side=LEFT)
mode_2_button.pack(side=LEFT)
mode_3_button.pack(side=LEFT)
mode_4_button.pack(side=LEFT)
mode_5_button.pack(side=LEFT)
mode_6_button.pack(side=LEFT)
dansmode1_button.pack(side=LEFT)
dansmode2_button.pack(side=BOTTOM)
dansmode3_button.pack(side=RIGHT)
prik_button.pack(side=TOP)
'''
'''
t2 = threading.Thread(target=while_jemoeder())
t2.start()
'''


print "voor de thread"
t = threading.Thread(target=win.mainloop())
t.start()
print "UI gestopt"
'''
win.mainloop()
'''
