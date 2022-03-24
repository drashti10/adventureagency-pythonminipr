from tkinter import *   
import tkinter as tk
import sys  
import os 
import invoice
scuba= tk.Tk()  
scuba.title("SCUBA")
scuba.geometry("1090x650")  
scuba.configure(bg='#000')
#img = PhotoImage(file="D:\\pythonminipr\\images\\scuba.jpg")
photo = PhotoImage(file = r"D:\pythonminipr\images\scuba.png")

lab = tk.Label(scuba, image=photo).place(
                  x=10,
                  y=150, 
                  height=500,
                  width=600,
                #  border='0',      
				  relx = 1.0,
                  rely = 0.1,
                  anchor ='e')
heading = Label(scuba,fg='white', text = "HOW MANY PEOPLE ARE THERE IN TOTAL?" , font = 'Verdana 25 bold',background='#000')
heading.place(x=55 , y=500)
p = Label(scuba, text = "How to reach? : From Delhi to goa via flight or train\n \n go to closest station or airport\n\nBest Time to Visit....\n\nThe best time to visit is between\n january and march when there is\n no rains and weather is pleasant.Popular Operators:\nPRICE - 6700" , font = 'Verdana 18 bold',background='#000',fg='white')
p.place(x=5, y=39)
x=Label(scuba,fg='white',text="What is Scuba Diving?",font='times 24 roman bold',background='#000')
x.place(x=1000,y=450)
desc=Label(scuba, text ="Scuba diving is mainly done for the\n attraction of the unattainable undersea world. \n It is one area of nature that mankind\n has not been able to fully control, we simply\n are not able to breathe underwater.\nHence, scuba diving gives us an opportunity\n to be in that underwater world,\n even if it is just for a limited amount of time.", font = 'Verdana 18 bold',background='#000',fg='white')
desc.place(x=970,y=500)
no_of_people= Label(scuba,fg='white', text= "SELECT NUMBER OF PEOPLE :" , font='Verdana 25 bold',background='#000')
no_of_people.place(x=55,y=600)
no_of_people =(Entry(scuba, width=40, textvariable = no_of_people))
no_of_people.place(x=605 , y=613)
no_of_people=(no_of_people.get())

btn_calc = Button(scuba, text = "TOTAL BILL" ,font='Verdana 25 bold')
btn_calc.place(x=600, y=703)
scuba.mainloop()
