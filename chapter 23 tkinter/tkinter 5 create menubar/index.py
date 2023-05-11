import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Making Menubar")


# **************************** simple menubar ******************************
def func():
    print("function is called")

# menu_bar = tk.Menu(window)
# menu_bar.add_command(label="Save", command=func)
# menu_bar.add_command(label="Save as", command=func)
# menu_bar.add_command(label="new file", command=func)
# menu_bar.add_command(label="open", command=func)

# window.config(menu=menu_bar)


# ****************************** Main menu ********************************

main_menu = tk.Menu(window)

#file menu

file_menu = tk.Menu(main_menu, tearoff=0)  # tearoff is to stop breaking the child bar from it's parents bar

file_menu.add_command(label="New file", command=func)
file_menu.add_command(label="Open", command=func)
file_menu.add_command(label="Open recent", command=func)
file_menu.add_separator()
file_menu.add_command(label="Save", command=func)
file_menu.add_command(label="Save as", command=func)

# edit menu

edit_menu = tk.Menu(main_menu, tearoff=0)
edit_menu.add_command(label="crop", command=func)
edit_menu.add_command(label="select & cut", command=func)
edit_menu.add_command(label="blur", command=func)



main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit", menu=edit_menu)




window.config(menu=main_menu)



window.mainloop()