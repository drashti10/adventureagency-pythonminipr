from tkinter import *   
import tkinter as tk
import sys  
import os 
riverrafting= tk.Tk()  
riverrafting.title("RIVER RAFTING")
riverrafting.geometry("1090x650")  
riverrafting.configure(bg='#000')
#img = PhotoImage(file="D:\\pythonminipr\\images\\bungee.jpg")
photo = PhotoImage(file = r"D:\pythonminiproject\images\riverrafting.png")

lab = tk.Label(riverrafting, image=photo).place(
                  x=100,
                  y=90, 
                  height=500,
                  width=600,
                #  border='0',      
				  relx = 1.0,
                  rely = 0.1,
                  anchor ='e')
heading = Label(riverrafting, background='black',fg='white',text = "HOW MANY PEOPLE ARE THERE IN TOTAL?" , font = 'Verdana 25 bold')
heading.place(x=100 , y=500)
p = Label(riverrafting, text = "River Ganga at Rishikesh Undoubtedly one of the most spectacular\n\n spots for White Water River rafting in India, Rishikesh has become\n\n a synonym for this thrilling adventure sport.\n\n Rishikesh nestled in Garhwal Himalaya in Uttarakhand \n\noffers rafting in the mighty and whimsical River Ganga \n\nin 4 stretches\n\nPRICE - 4000" , font = 'Verdana 18 bold',background='#000',fg='white')
p.place(x=5, y=39)
x=Label(riverrafting,fg='white',text="What is River rafting?",font='times 24 roman bold',background='#000')
x.place(x=1000,y=450)
desc=Label(riverrafting, text ="Rafting, the high-adrenaline sport of navigating\n a river in an inflatable raft, involves\n several levels of difficulty, depending\n on how choppy the river is. These ‘grades’\n of difficulty are arrived at according to \nthe presence of rapids, which evolve due\n to sudden plunges in the river’s \nheight, and also because of rocks \n– small or large – that may\n be lurking in the waters.\n Rafting is a challenging but tremendously \nfun activity", font = 'Verdana 18 bold', background='black',fg='white')
desc.place(x=920,y=500)
no_of_people= Label(riverrafting, text= "SELECT NUMBER OF PEOPLE :" , font='Verdana 25 bold', background='black',fg='white')
no_of_people.place(x=55,y=600)
no_of_people= IntVar(riverrafting)
no_of_people = Entry(riverrafting, width=40, textvariable = no_of_people)
no_of_people.place(x=605 , y=613)
btn_calc = Button(riverrafting, text = "TOTAL BILL" ,font='Verdana 25 bold', background='black',fg='white')
btn_calc.place(x=600, y=703)
riverrafting.mainloop()