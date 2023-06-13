import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Miles to Kilomitre Converter")
window.config(padx=20,pady=20)

def action():
    miles_qu = miles.get()
    kilom = round(miles_qu*1.61,2)
    km.config(text=f"{kilom}")


label_miles = ttk.Label(window, text="Miles")
label_miles.grid(column=2, row=0)

miles = tk.IntVar()
miles_entry = ttk.Entry(window, textvariable=miles, width=7)
miles_entry.grid(column=1,row=0)

label_km = ttk.Label(window, text="equal to")
label_km.grid(column=0,row=1)

km = ttk.Label(window, text="")
km.grid(column=1,row=1)

label_kms = ttk.Label(window, text="Km")
label_kms.grid(column=2,row=1)

submit = ttk.Button(window, text="Convert", command=action)
submit.grid(column=1,row=2)


for child in window.winfo_children():
    child.grid_configure(pady=5, padx=2)












window.mainloop()