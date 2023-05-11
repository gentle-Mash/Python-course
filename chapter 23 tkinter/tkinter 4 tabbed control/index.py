import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Tabbed Control")

nb = ttk.Notebook(win)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)

nb.add(page1, text="page-1")
nb.add(page2, text="page-2")

nb.pack(expand=True, fill="both")

name_label = ttk.Label(page1, text="Enter your name: ")
name_label.grid(row=0, column=0, sticky=tk.W)

name_var = tk.StringVar()
name_entrybox = ttk.Entry(page1, width=18, textvariable=name_var)
name_entrybox.focus()
name_entrybox.grid(row=0, column=1)


age_label = ttk.Label(page2, text="Enter your age: ")
age_label.grid(row=0, column=0, sticky=tk.W)

age_var = tk.IntVar()
age_entrybox = ttk.Entry(page2, width=18, textvariable=age_var)
age_entrybox.grid(row=0, column=1)


win.mainloop()