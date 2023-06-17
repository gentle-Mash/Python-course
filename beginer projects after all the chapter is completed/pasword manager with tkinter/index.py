import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
from generate_password import generate
import pyperclip

########################################## FUNCTIONALITY ###################################

def storing_data():
    user_info = user_entry_var.get()
    website_info = website_entry_var.get()
    password_info = password_entry_var.get()

    if user_info == "" or website_info == "" or password_info == "":
        m_box.showinfo("Error", "you didn't fill every box")
    else:
        is_ok = m_box.askyesnocancel(title="Information", message=f"Do you want to save it?")

        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website_info} | {user_info} | {password_info}\n")

        website_entry.delete(0,tk.END)
        user_entry.delete(0,tk.END)
        password_entry.delete(0,tk.END)


def geberating_pass():
    password = generate()
    password_entry.insert(0, password)
    pyperclip.copy(password)


########################################## UI SETUP ###################################

window = tk.Tk()
window.title("Password Manager")
window.config(padx=60,pady=50)

canvas = tk.Canvas(window, width=200, height=200)
lock_image = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = lock_image)
canvas.grid(column=1, row=0)

website_label = ttk.Label(window, text="Website ")
website_label.grid(column=0, row=1)

website_entry_var = tk.StringVar()
website_entry = ttk.Entry(window, width=45, textvariable= website_entry_var)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

user_or_email_label = ttk.Label(window, text="Email/Usernmae: ")
user_or_email_label.grid(column=0, row=2)

user_entry_var = tk.StringVar()
user_entry = ttk.Entry(window, width=45, textvariable= user_entry_var)
user_entry.grid(column=1, row=2, columnspan=2)

password_label = ttk.Label(window, text="Password: ")
password_label.grid(column=0, row=3)

password_entry_var = tk.StringVar()
password_entry = ttk.Entry(window, width= 32, textvariable= password_entry_var)
password_entry.grid(column=1, row=3)

generate_button = ttk.Button(window,text="Generate", command= geberating_pass)
generate_button.grid(column=2, row=3)

add_button = ttk.Button(window, text="Add", width=45, command= storing_data)
add_button.grid(column=1, row=4, columnspan=2)

for child in window.winfo_children():
    child.grid_configure(pady=3)

window.mainloop()