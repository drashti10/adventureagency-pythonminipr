from tkinter import *   
import tkinter as tk
import sys  
import os 
from tkinter import ttk, messagebox
import invoice
rock_climb= tk.Tk()  
rock_climb.title("ROCK CLIMB")
rock_climb.geometry("1090x650")  
rock_climb.configure(bg='#000')
#img = PhotoImage(file="D:\\pythonminipr\\images\\rock_climb.jpg")
photo = PhotoImage(file = r"D:\pythonminiproject\images\rockclimbing.png")

lab = tk.Label(rock_climb, image=photo).place(
                  x=100,
                  y=90, 
                  height=500,
                  width=600,
                #  border='0',      
				  relx = 1.0,
                  rely = 0.1,
                  anchor ='e')
heading = Label(rock_climb, fg='white',text = "HOW MANY PEOPLE ARE THERE IN TOTAL?" , font = 'Verdana 25 bold',background='#000')
heading.place(x=55 , y=500)
p = Label(rock_climb, text = "How to reach? : From Delhi to Alps via flight \n nearest airport at Europe.\n\nBest Time to Visit....\n\nThe best time to visit is between\n October and mid-June when there is\n no rains and weather is pleasant.Popular Operators:\nPRICE - 7900" , font = 'Verdana 18 bold',background='#000',fg='white')
p.place(x=5, y=39)
x=Label(rock_climb,fg='white',text="What is Rock Climbing?",font='times 24 roman bold',background='#000')
x.place(x=1000,y=450)
desc=Label(rock_climb,fg='white', text ="Rock climbing is the sport or activity of \nclimbing rock faces, especially with the aid of\n ropes and special equipment. The\n concept is to reach an end point, or\n a summit, of a rock face or structure.\n This can be done with specific equipment,\n depending on the difficulty and severity of the climb", font = 'Verdana 18 bold',background='#000')
desc.place(x=870,y=500)
no_of_people= Label(rock_climb, text= "SELECT NUMBER OF PEOPLE :" , fg='white',font='Verdana 25 bold',background='#000')
no_of_people.place(x=55,y=600)
no_of_people =Entry(rock_climb, width=40, textvariable = no_of_people)
no_of_people.place(x=605 , y=613)
no_of_people=(no_of_people.get())

btn_calc = Button(rock_climb, text = "TOTAL BILL" ,font='Verdana 25 bold')
messagebox.showinfo("Success" , "BOOKING CONFIRMED" , parent = rock_climb)
btn_calc.place(x=600, y=703)
rock_climb.mainloop()


