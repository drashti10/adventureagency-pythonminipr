from tkinter import *
import tkinter.messagebox as tkMessageBox
import mysql.connector
from mysql.connector import Error
from tkinter import ttk, messagebox
import os
import sys
def action():
        if first_name.get()=="" or last_name.get()=="" or age.get()=="" or city.get()=="" or add.get()=="" or user_name.get()=="" or password.get()=="" or very_pass.get()=="":
            messagebox.showerror("Error" , "All Fields Are Required" , parent = winsignup)
        elif password.get() != very_pass.get():
            messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = winsignup)
        else:
            try:
                con = mysql.connector.connect(host="localhost",user="root",password="",database="adventure_agency")
                cur = con.cursor()
                query="select user_name from user_information where 'user_name'=%s"
                row1=user_name.get()
                row=cur.execute(query,(row1,))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error" , "User Name Already Exits", parent = winsignup)
                else:
                    cur.execute("insert into user_information(first_name,last_name,age,gender,city,address,user_name,password) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                        first_name.get(), 
                        last_name.get(),
                        age.get(),
                        var.get(),
                        city.get(),
                        add.get(),
                        user_name.get(),
                        password.get()
                        ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success" , "Ragistration Successfull" , parent = winsignup)
                    clear()
                    switch()
                
            except Exception as es:
                messagebox.showerror("Error" , f"Error Dui to : {str(es)}", parent = winsignup)

         
def switch():
        winsignup.destroy()

def clear():
    first_name.delete(0,END)
    last_name.delete(0,END)
    age.delete(0,END)
    var.set("Male")
    city.delete(0,END)
    add.delete(0,END)
    user_name.delete(0,END)
    password.delete(0,END)
    very_pass.delete(0,END)
winsignup = Tk()
winsignup.title("ADVENTURE AGENCY")
winsignup.configure(bg='#000')
winsignup.maxsize(width=500 ,  height=600)
winsignup.minsize(width=500 ,  height=600)
   #heading label
heading = Label(winsignup , text = "Signup" , font = 'Helvetica 20 bold',fg='white',background='black')
heading.place(x=100 , y=60)

first_name = Label(winsignup, text= "First Name :" , font='Verdana 10 bold',fg='white',background='black')
first_name.place(x=80,y=130)
last_name = Label(winsignup, text= "Last Name :" , font='Verdana 10 bold',fg='white',background='black')
last_name.place(x=80,y=160)

age = Label(winsignup, text= "Age :" , font='Verdana 10 bold',fg='white',background='black')
age.place(x=80,y=190)

Gender = Label(winsignup, text= "Gender :" , font='Verdana 10 bold',fg='white',background='black')
Gender.place(x=80,y=220)

city = Label(winsignup, text= "City :" , font='Verdana 10 bold',fg='white',background='black')
city.place(x=80,y=260)

add = Label(winsignup, text= "Address :" , font='Verdana 10 bold',fg='white',background='black')
add.place(x=80,y=290)

user_name = Label(winsignup, text= "User Name :" , font='Verdana 10 bold',fg='white',background='black')
user_name.place(x=80,y=320)

password = Label(winsignup, text= "Password :" , font='Verdana 10 bold',fg='white',background='black')
password.place(x=80,y=350)

very_pass = Label(winsignup, text= "Verify Password:" , font='Verdana 10 bold',fg='white',background='black')
very_pass.place(x=80,y=380)

first_name = StringVar()
last_name = StringVar()
age = IntVar(winsignup, value='0')
var= StringVar()
city= StringVar()
add = StringVar()
user_name = StringVar()
password = StringVar()
very_pass = StringVar()


first_name = Entry(winsignup, width=40 , textvariable = first_name)
first_name.place(x=200 , y=133)    
last_name = Entry(winsignup, width=40 , textvariable = last_name)
last_name.place(x=200 , y=163)
age = Entry(winsignup, width=40, textvariable=age)
age.place(x=200 , y=193)    
Radio_button_male = ttk.Radiobutton(winsignup,text='Male', value="Male", variable = var).place(x= 200 , y= 220)
Radio_button_female = ttk.Radiobutton(winsignup,text='Female', value="Female", variable = var).place(x= 200 , y= 238)
city = Entry(winsignup, width=40,textvariable = city)
city.place(x=200 , y=263)
add = Entry(winsignup, width=40 , textvariable = add)
add.place(x=200 , y=293)
user_name = Entry(winsignup, width=40,textvariable = user_name)
user_name.place(x=200 , y=323)
password = Entry(winsignup, width=40, textvariable = password)
password.place(x=200 , y=353)
very_pass= Entry(winsignup, width=40 ,show="*" , textvariable = very_pass)
very_pass.place(x=200 , y=383)
btn_signup = Button(winsignup, text = "Signup" ,font='Verdana 10 bold', command = action)
btn_signup.place(x=200, y=413)
btn_login = Button(winsignup, text = "Clear" ,font='Verdana 10 bold' , command = clear)
btn_login.place(x=280, y=413)
def switch():
    os.system('loginmain.py')
sign_up_btn = Button(winsignup , text="Switch To Login" , command = switch )
sign_up_btn.place(x=350 , y =20)
winsignup.mainloop()
                
