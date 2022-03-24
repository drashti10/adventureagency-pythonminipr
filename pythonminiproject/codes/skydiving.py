from tkinter import *   
import tkinter as tk
import sys  
import os 
skydiving= tk.Tk()  
skydiving.title("SKYDIVING")
skydiving.geometry("1090x650")  
skydiving.configure(bg='#000')
photo = PhotoImage(file = r"D:\pythonminiproject\images\sky.png")

lab = tk.Label(skydiving, image=photo).place(
                  x=80,
                  y=90, 
                  height=500,
                  width=600,     
                  relx = 1.0,
                  rely = 0.1,
                  anchor ='e')
heading = Label(skydiving,fg='white', text = "HOW MANY PEOPLE ARE THERE IN TOTAL?" , font = 'Verdana 25 bold',background='black')
heading.place(x=100 , y=500)
p = Label(skydiving, text = "Aamby Valley Maharashtra Aamby Valley, Maharashtra - Best Spot\n\n for Skydiving in India. Aamby Valley in\n\n Maharashtra is the top sky diving spot in India,\n\n especially for a tandem jump. If you are an\n \navid skydiver, this place also offers membership\n\n which will allow you to go for skydiving all round the year.\nPRICE - 12000" , font = 'Verdana 18 bold',background='#000',fg='white')
p.place(x=5, y=39)
x=Label(skydiving,fg='white',text="What is skydiving?",font='times 24 roman bold',background='#000')
x.place(x=1000,y=450)
desc=Label(skydiving, text ="Typical jump altitudes in modern times\n for experienced skydivers range\n from 7,500 to 15,000 feet (2,300 to 4,600 \nmetres) above ground level, yielding a freefall \ntime of between 40 and 85 seconds. The length \nof the freefall (the time between exiting\n the aircraft and deploying the parachute) \nis dependent upon such factors \nas exit altitude, opening altitude, and fall rate.", font = 'Verdana 18 bold',fg='white',background='black')
desc.place(x=970,y=500)
no_of_people= Label(skydiving, text= "SELECT NUMBER OF PEOPLE :" , font='Verdana 25 bold',background='black',fg='white')
no_of_people.place(x=55,y=600)
no_of_people= IntVar(skydiving)
no_of_people = Entry(skydiving, width=40, textvariable = no_of_people)
no_of_people.place(x=605 , y=613)
btn_calc = Button(skydiving, text = "TOTAL BILL" ,font='Verdana 25 bold')
btn_calc.place(x=600, y=703)
skydiving.mainloop()
