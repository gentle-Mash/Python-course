import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("LOOP")

labels = ["Enter your name: ", "enter your age: ", "address: ", "religion: ", "nationality: ", "yearly-income: "]
# label_var_names = ["name","age","add","rel","nation","income"]

for i in range(len(labels)):
    current_label = ttk.Label(win, width=16, text=labels[i])
    current_label.grid(row=i,column=0, sticky = tk.W)

entrybox = {
    'name_entry':tk.StringVar(),
    'age-entry':tk.IntVar(),
    'add-entry':tk.StringVar(),
    'rel-entry':tk.StringVar(),
    'nation-entry':tk.StringVar(),
    'income-entry':tk.IntVar()
}
counter = 0
for i in entrybox:
    current_box = ttk.Entry(win, width=16, textvariable=entrybox[i])
    current_box.grid(column=3, row=counter, sticky=tk.W)
    counter +=1

def action():
    print(entrybox["name_entry"].get())
    print(entrybox["age-entry"].get())
    print(entrybox["add-entry"].get())

submit_button = ttk.Button(win, width=13, text="Submit", command=action)
submit_button.grid(row=counter+1, column=0, sticky=tk.W)


win.mainloop()