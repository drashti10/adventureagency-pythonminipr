from tkinter import *   
import tkinter as tk
import sys  
import os 
import invoice
gliding= tk.Tk()  
gliding.title("PARAGLIDING")
gliding.geometry("1090x650")  
gliding.configure(bg='#000')
#img = PhotoImage(file="D:\\pythonminipr\\images\\gliding.jpg")
photo = PhotoImage(file = r"D:\pythonminipr\images\paragliding.png")

lab = tk.Label(gliding, image=photo).place(
                  x=10,
                  y=90, 
                  height=450,
                  width=600,
                  relx = 1.0,
                  rely = 0.1,
                  anchor ='e')
heading = Label(gliding, text = "HOW MANY PEOPLE ARE THERE IN TOTAL?" ,fg='white', font = 'Verdana 25 bold',background='#000')
heading.place(x=55 , y=500)
p = Label(gliding, text = "How to reach? : From Delhi to Bir via buses \n(Volvo or Tata) or flights to the\n nearest airport at Dharamshala.\n\nBest Time to Visit....\n\nThe best time to visit is between\n October and mid-June when there is\n no rains and weather is pleasant.Popular Operators:\nCamp Oak View, Friends adventures, and tours, Blue Umbrella\nPRICE - 7500" , font = 'Verdana 18 bold',background='#000',fg='white')
p.place(x=5, y=39)
x=Label(gliding,text="What is Para gliding?",font='times 24 roman bold',background='#000',fg='white')
x.place(x=1000,y=450)
desc=Label(gliding,fg='white', text ="Paragliding,sport of flying parachutes with\n design modifications that enhance \ntheir gliding capabilities. Unlike hang \ngliders, their close relations, paragliders\n have no rigid framework; the parachute\n canopy acts as a wing and is constructed of\n fabric cells with openings at the front that allow\n them to be inflated by movement through the air", font = 'Britannic 18 bold',foreground='white',background='#000')
desc.place(x=1000,y=500)
no_of_people=IntVar()
no_of_people= Label(gliding, text= "SELECT NUMBER OF PEOPLE :" ,fg='white', font='Verdana 25 bold',background='#000')
no_of_people.place(x=55,y=600)
no_of_people =Entry(gliding, width=40, textvariable = no_of_people)
no_of_people.place(x=605 , y=613)
x=no_of_people.get()
print ('total is ',x)
btn_calc = Button(gliding, text = "TOTAL BILL" ,font='Verdana 25 bold')
btn_calc.place(x=600, y=703)
gliding.mainloop()

