from tkinter import *   
import sys  
import os
top = Tk()  
  
top.geometry("1090x650")  
top.configure(bg='#000000')
heading = Label(top, text = "WHAT ACTIVITY WOULD YOU LIKE TO PERFORM ?" , font = 'Verdana 25 bold')
heading.place(x=80 , y=150)
def bungee():
	os.system("bungee.py")	
btn_signup = Button(top, text = "BUNGEE JUMPING" ,font='Verdana 10 bold',height = 4,width = 15,command=bungee)
btn_signup.place(x=200, y=230)
def riverrafting():
	os.system("riverrafting.py")
btn_signup = Button(top, text = "RIVER RAFTING" ,font='Verdana 10 bold',height = 4,width = 15,command=riverrafting)
btn_signup.place(x=200, y=360)
def skydiving():
	os.system("skydiving.py")	
btn_signup = Button(top, text = "SKY DIVING" ,font='Verdana 10 bold',height = 4,width = 15 , command=skydiving)
btn_signup.place(x=200, y=510)
def scuba():
	os.system("scuba.py")	
btn_signup = Button(top, text = "SCUBA DIVING" ,font='Verdana 10 bold',height = 4,width = 15,command=scuba)
btn_signup.place(x=500, y=230)
def gliding():
	os.system("gliding.py")	
btn_signup = Button(top, text = "PARA GLIDING" ,font='Verdana 10 bold',height = 4,width = 15,command=gliding)
btn_signup.place(x=500, y=360)
def rock_climbing():
	os.system("reck_climbing.py")	
btn_signup = Button(top, text = "ROCK CLIMBING" ,font='Verdana 10 bold',height = 4,width = 15,command=rock_climbing)
btn_signup.place(x=500, y=510)
  
top.mainloop() 