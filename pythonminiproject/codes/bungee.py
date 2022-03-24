from tkinter import *   
import tkinter as tk
import sys  
import os 
import invoice
bungee= tk.Tk()  
bungee.title("BUNGEE")
bungee.geometry("1090x650")  
bungee.configure(bg='#000')
#img = PhotoImage(file="D:\\pythonminipr\\images\\bungee.jpg")
photo = PhotoImage(file = r"D:\pythonminiproject\images\bungee.png")

lab = tk.Label(bungee, image=photo).place(
                  x=100,
                  y=90, 
                  height=500,
                  width=600,
                #  border='0',      
				  relx = 1.0,
                  rely = 0.1,
                  anchor ='e')
heading = Label(bungee, fg='white',background='black',text = "HOW MANY PEOPLE ARE THERE IN TOTAL?" , font = 'Verdana 25 bold')
heading.place(x=100 , y=500)
p = Label(bungee, text = "Della Adventures in Lonavala, Maharashtra A small hill station on the\n\n outskirts of Pune, a beautiful place and a perfect one for Bungee Jumping \n\nin India which takes place in an adventure park called \n\nDella Adventures. The equipment is attached at a height \n\nof 150 ft and lasts for about 7-10 minutes.\n\nPRICE - 12000" , font = 'Verdana 18 bold',background='#000',fg='white')
p.place(x=5, y=39)
x=Label(bungee,fg='white',text="What is bungeejumping?",font='times 24 roman bold',background='#000')
x.place(x=1000,y=450)
desc=Label(bungee, text ="Bungee jumping is an adventurous sport in which \npeople jump from higher ground such as\n a bridge with an elastic rope tied to their ankles \nto stop them from hitting the ground.\n The rope is designed to stretch,\n not break. When the rope has stretched \nall the way, the jumper bounces back\n up. When people jump they wear safety equipment \nlike helmets and a harness\n", font = 'Verdana 18 bold',background='#000',fg='white')
desc.place(x=920,y=500)
no_of_people= Label(bungee, text= "SELECT NUMBER OF PEOPLE :" , fg='white',background='black',font='Verdana 25 bold')
no_of_people.place(x=55,y=600)
no_of_people =(Entry(bungee, width=40, textvariable = no_of_people))
no_of_people.place(x=605 , y=613)
no_of_people=(no_of_people.get())
btn_calc = Button(bungee, text = "TOTAL BILL" ,font='Verdana 25 bold',fg='white',background='black')
btn_calc.place(x=600, y=703)
bungee.mainloop()