from tkinter import *   
import tkinter as tk
import os
import sys
homepg= tk.Tk()  
homepg.title("HOME PAGE")
homepg.geometry("1090x650")  
homepg.configure(bg='#000')
photo = PhotoImage(file = r"D:\pythonminiproject\images\advawaits.png")

lab = tk.Label(homepg, image=photo).place(
                  x=1,
                  y=1, 
                  height=700,
                  width=1900,
                #  border='0',      
				  relx = 1.0,
                  rely = 0.1,
                  anchor ='ne')

heading = Label(homepg , text = "ADVENTURE AWAITS" , font = 'Harrington 55 bold',fg='white',background='black')
heading.place(x=500 , y=100)


def logincall():
	os.system("loginmain.py")	
btn_signup = Button(homepg, text = "LOGIN" ,font='Verdana 10 bold',height = 4,width = 15,command=logincall)
btn_signup.place(x=600, y=430)

def registcall():
	os.system("register.py")	
btn_signup = Button(homepg, text = "REGISTER" ,font='Verdana 10 bold',height = 4,width = 15,command=registcall)
btn_signup.place(x=200, y=430)
homepg.mainloop()