import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box

window = tk.Tk()
window.title("GUI message")

# labelframe

label_frame = ttk.LabelFrame(window, text="Please fill this form")
label_frame.grid(row=0,column=0)
#lebels

name_label = ttk.Label(label_frame, text="Enter your name: ", font=("Helvetica",11 ))
age_label = ttk.Label(label_frame, text="Enter your age: ", font=("Helvetica",11 ))

#entry box

name_var = tk.StringVar()
name_entry = ttk.Entry(label_frame, width=20, textvariable=name_var)
name_entry.focus()

age_var = tk.StringVar()
age_entry = ttk.Entry(label_frame, width=20, textvariable=age_var)

#grid
name_label.grid(row=0,column=0, sticky=tk.W, padx=4,pady=2)
name_entry.grid(row=1,column=0, sticky=tk.W, padx=4,pady=2)
age_label.grid(row=0, column=1, sticky=tk.W, padx=4,pady=2)
age_entry.grid(row=1, column=1, sticky=tk.W, padx=4,pady=2)


def func():
    name = name_var.get()
    age = age_var.get()

    if name == "" or age == "":
        m_box.showerror("Error","Please fill the BOX")
    else:
        try:
           age = int(age)
        except ValueError:
            m_box.showerror("ValueError","Only digits are allowed in age box")
        else:
            print(f"{name} is {age} years old")
    
    name_entry.delete(0, tk.END)
    age_entry.delete(0,tk.END)
    name_entry.focus()


submit_button = ttk.Button(label_frame, text="Submit", command=func)
submit_button.grid(row=2, columnspan=2)






window.mainloop()