# while working with tkinter you always have to write this 3-4 lines 
# 1 you can import tkinter module in one of these ways
# a) import tkinter
# b) import tkinter as tk ---> try to use this way 
# c) from tkinter import *

import tkinter as tk
from tkinter import ttk
from csv import writer
import os
# 2 declare your window variable with Tk() class 
window = tk.Tk() # if you use way no c) then you don't have to write tk.Tk() just write TK()

# 3 make endless loop of this appliscation with mainloop class
# like --- window.mainloop()
# and other everything you will erite before this mainloop()

window.title("GUI")
# crate lables, buttons, radio buttons and other widgets for this you have to import another 
# package of tkinter and that is ttk . though you can work with tk alone but ttk will give us a betther view of our widgets

name_label = ttk.Label(window, text="Enter your name: ") # here we are just defining that in our app there will be label but we didn't give our location of where the label will show up
# for that you can use either pack or grid or palce method 
# pack will centerize your label but with grid you can manipulate your label
name_label.grid(row=0,column=0, sticky=tk.W)

email_label = ttk.Label(window, text="Enter your email: ")
email_label.grid(row=1, column=0, sticky=tk.W)

age_label = ttk.Label(window, text="Enter your age: ")
age_label.grid(row=2,column=0, sticky=tk.W) # here sticky is for keep the alingment left side means west side

gender_label = ttk.Label(window, text="Select your gender: ")
gender_label.grid(row=3,column=0, sticky=tk.W)

hobby_label = ttk.Label(window, text="What is your hobby: ")
hobby_label.grid(row=4,column=0, sticky=tk.W)
# we will talk about this methods more when we will work with styling our application

# make entry box
name_var = tk.StringVar()
name_entrybox = ttk.Entry(window, width=16, textvariable=name_var)
name_entrybox.grid(row=0, column=1)
name_entrybox.focus()

email_var = tk.StringVar()
email_entrybox = ttk.Entry(window, width=16, textvariable=email_var)
email_entrybox.grid(row=1, column=1)

age_var = tk.IntVar()
age_entrybox = ttk.Entry(window, width=16, textvariable=age_var,)
age_entrybox.grid(row=2, column=1)


#making combo box

gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(window, width=13, textvariable=gender_var, state="readonly") # here state is for no writing in the box
gender_combobox["values"] = ("male", "female", "other")
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)


# making radio buttons

hobby_var = tk.StringVar()
hobby_radiobutton1 = ttk.Radiobutton(window, text="Drawing", value="Drawing", variable=hobby_var)
hobby_radiobutton1.grid(row=4,column=1, sticky=tk.W)
hobby_radiobutton2 = ttk.Radiobutton(window, text="Gaming", value="Gaming", variable=hobby_var)
hobby_radiobutton2.grid(row=5,column=1, sticky=tk.W)
hobby_radiobutton3 = ttk.Radiobutton(window, text="Gardening", value="Gardening", variable=hobby_var)
hobby_radiobutton3.grid(row=6,column=1, sticky=tk.W)


# check buttons

check_var = tk.IntVar()
check_button = ttk.Checkbutton(window, text="if you agree with our privecy policy, check this box", variable=check_var)
check_button.grid(row=7, columnspan=5) # columnspan is stopping check_button to interfare with other's column


# make buttons

# def action():  for making text files
#     name = name_var.get()
#     email =email_var.get()
#     age = age_var.get()
#     gender = gender_var.get()
#     hobby = hobby_var.get()
#     var = check_var.get()
#     if var == 1:
#         check = "checked"
#     else:
#         check = "unchecked"
#     print(f"{name} is {age} years old, gender is {gender}, hobby is {hobby} and email is {email}. {check}")
#     with open("file.txt", "a") as text_file:
#         text_file.write(f"{name},{age},{gender},{hobby},{email},{check}\n")
    
#     name_entrybox.delete(0, tk.END)
#     age_entrybox.delete(0, tk.END)
#     email_entrybox.delete(0, tk.END)

#     name_label.configure(foreground="Red")

def action(): #for csv files
    name = name_var.get()
    email =email_var.get()
    age = age_var.get()
    gender = gender_var.get()
    hobby = hobby_var.get()
    var = check_var.get()
    if var == 1:
        check = "checked"
    else:
        check = "unchecked"
    print(f"{name} is {age} years old, gender is {gender}, hobby is {hobby} and email is {email}. {check}")
    
    with open("file.csv", "a", newline="") as sid:
        mithai = writer(sid)
        if os.stat("file.csv").st_size == 0:
            mithai.writerow(["user name","age","gender","hobby","email","check"])
        mithai.writerow([name,age,gender,hobby,email,check])
    
    name_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)

    name_label.configure(foreground="Red")

submit_button = ttk.Button(window, text="Submit", command=action)
submit_button.grid(row=8,column=0, sticky=tk.W)






window.mainloop()