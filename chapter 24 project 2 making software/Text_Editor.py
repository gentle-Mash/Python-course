import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
from tkinter import colorchooser, font, filedialog
import os


window = tk.Tk()
window.geometry("1000x600")
window.title("Text Editor")


# *************************************** main menu **********************************

main_menu = tk.Menu(window)

# file icons
new_icon = tk.PhotoImage(file="new file.png")
open_icon = tk.PhotoImage(file="open file.png")
save_icon = tk.PhotoImage(file="save.png")
save_as_icon = tk.PhotoImage(file="save as.png")
exit_icon = tk.PhotoImage(file="exit.png")



# ************************************** file menu functionality *****************************



#file functionality
file_menu = tk.Menu(main_menu, tearoff=False)

# New file function
url = ""
def new_file(event = None):
    global url
    url = ""
    text_editor.delete(1.0, tk.END)

# new file command
file_menu.add_command(label="New file", image=new_icon, command=new_file, compound=tk.LEFT,accelerator="Ctrl+N")

# open function
def open_file(event = None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file", filetypes=(('text files', '*.txt'),('all files','*.*')))
    try:
        with open(url,"r") as rf:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0, rf.read())
    except FileNotFoundError:
        return
    except:
        return
    window.title(os.path.basename(url))
    
# open file command
file_menu.add_command(label="Open", image=open_icon,command=open_file ,compound=tk.LEFT,accelerator="Ctrl+O")


# save file function
def save_file(event = None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url,"w", encoding="UTF-8") as wf:
                wf.write(content)
        else:
            url = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=(('text files', '*.txt'),('all files','*.*')))
            content2 = str(text_editor.get(1.0,tk.END))
            url.write(content2)
            url.close()
    except:
        return
    
# save file command            
file_menu.add_command(label="Save", image=save_icon, command=save_file, compound=tk.LEFT,accelerator="Ctrl+S")


# save as file function
def save_as(event=None):
    global url
    try:
        url = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=(('text files', '*.txt'),('all files','*.*')))
        content2 = str(text_editor.get(1.0,tk.END))
        url.write(content2)
        url.close()
    except:
        return

# save as file command
file_menu.add_command(label="Save as", image=save_as_icon, compound=tk.LEFT, command=save_as, accelerator="Ctrl+Shift+S")



# edit icons
copy_icon = tk.PhotoImage(file="copy.png")
paste_icon = tk.PhotoImage(file="paste.png")
cut_icon = tk.PhotoImage(file="cut.png")
clear_icon = tk.PhotoImage(file="clear.png")
find_icon = tk.PhotoImage(file="find.png")

# edit commands and functions
edit_menu = tk.Menu(main_menu, tearoff=False)

edit_menu.add_command(label="Copy", image=copy_icon, compound=tk.LEFT, accelerator="Ctrl+C", command= lambda:text_editor.event_generate("<Control c>"))

edit_menu.add_command(label="Paste", image=paste_icon, compound=tk.LEFT, accelerator="Ctrl+V", command= lambda:text_editor.event_generate("<Control v>"))

edit_menu.add_command(label="Cut", image=cut_icon, compound=tk.LEFT, accelerator="Ctrl+X", command= lambda:text_editor.event_generate("<Control x>"))


def clear_text(event=None):
    text_editor.delete(1.0, tk.END)

edit_menu.add_command(label="Clear", image=clear_icon, compound=tk.LEFT, accelerator="Ctrl+R", command= clear_text)


# find funtionality
def find_content(event=None):
    def find():
        word = find_entrybox.get()
        text_editor.tag_remove('match','1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex= tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                text_editor.tag_add('match', start_pos, end_pos)
                matches +=1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')
    
    def replace():
        word = find_entrybox.get()
        replace_text = replace_entrybox.get()
        content = text_editor.get(1.0,tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)



    find_dialogue = tk.Toplevel()
    find_dialogue.geometry("450x250+500+200")
    find_dialogue.title("Find")
    find_dialogue.resizable(0,0)

    #label frame
    find_framebox = ttk.LabelFrame(find_dialogue, text="Find/Replace")
    find_framebox.pack(pady=20)

    #labels
    find_label = ttk.Label(find_framebox, text="find: ")
    replace_label = ttk.Label(find_framebox, text="replace: ")

    # entrybox
    find_entrybox = ttk.Entry(find_framebox, width=30)
    replace_entrybox = ttk.Entry(find_framebox, width=30)

    # grids
    find_label.grid(row=0,column=0, padx=4,pady=4)
    replace_label.grid(row=0,column=1, padx=4,pady=4)
    find_entrybox.grid(row=1,column=0, padx=4,pady=4)
    replace_entrybox.grid(row=1,column=1, padx=4,pady=4)

    #buttons
    find_btn = ttk.Button(find_framebox, text="Find", command=find)
    replace_btn = ttk.Button(find_framebox, text="Replace", command=replace)

    #button grids
    find_btn.grid(row=2, column=0, padx=8, pady=4)
    replace_btn.grid(row=2, column=1, padx=8, pady=4)


    find_dialogue.mainloop()


edit_menu.add_command(label="Find", image=find_icon, compound=tk.LEFT,command=find_content, accelerator="Ctrl+F")




# view icons
tool_icon = tk.PhotoImage(file="tool bar.png")
status_icon = tk.PhotoImage(file="status bar.png")

# view commands
view_menu = tk.Menu(main_menu, tearoff=False)


show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)

def hide_toolbar(event=None):
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        staus_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        staus_bar.pack(side=tk.BOTTOM, fill=tk.X)
        show_toolbar = True



def hide_statusbar(event=None):
    global show_statusbar
    if show_statusbar:
        staus_bar.pack_forget()
        show_statusbar =False
    else:
        staus_bar.pack(side=tk.BOTTOM, fill=tk.X)
        show_statusbar = True



view_menu.add_checkbutton(label="Tool Bar", image=tool_icon, compound=tk.LEFT,variable=show_toolbar,onvalue=True, offvalue=False, command=hide_toolbar, accelerator="Ctrl+T")
view_menu.add_checkbutton(label="Status Bar", image=status_icon, compound=tk.LEFT,variable=show_statusbar,onvalue=True, offvalue=False, command=hide_statusbar, accelerator="Ctrl+Alt+S")


#color icons
default_icon = tk.PhotoImage(file="default.png")
dark_icon = tk.PhotoImage(file="dark.png")
# color codes

theme_choice = tk.StringVar()
colors = (default_icon, dark_icon)
color_dict = {
    "Light mode":("#000000", "#ffffff"),
    "Dark mode": ("#c4c4c4","#2d2d2d" )
}
count = 0
# color theme commands
color_theme_menu = tk.Menu(main_menu, tearoff=False)

def theme_change():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, foreground=fg_color)


for i in color_dict:    
    color_theme_menu.add_radiobutton(label=i, image=colors[count], compound=tk.LEFT, variable=theme_choice, command= theme_change)
    count += 1

    
# cascading

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit", menu=edit_menu)
main_menu.add_cascade(label="View", menu=view_menu)
main_menu.add_cascade(label="Color theme", menu=color_theme_menu)
# ************************************** End Main menu ************************************



# ************************************** tool bar ********************************************

tool_bar = ttk.Label(window)  #here you could have also tried label frame
tool_bar.pack(side=tk.TOP, fill=tk.X)

# font combobox

font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state="readonly")
font_box["values"] = font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0,column=0, padx=5)


# size box

size_var = tk.IntVar()
size_box = ttk.Combobox(tool_bar, width=14, textvariable=size_var, state="readonly")
size_box["values"] = tuple(range(7,81))
size_box.current(3)
size_box.grid(row=0, column=1, padx=5)

# button icons

bold_icon = tk.PhotoImage(file="bold.png")
italic_icon = tk.PhotoImage(file="italic.png")
underlined_icon = tk.PhotoImage(file="underlined.png")
color_icon = tk.PhotoImage(file="color.png")
left_icon = tk.PhotoImage(file="left.png")
centre_icon = tk.PhotoImage(file="centre.png")
right_icon = tk.PhotoImage(file="right.png")
justify_icon = tk.PhotoImage(file="justify.png")

#buttons

bold_btn = ttk.Button(tool_bar, image=bold_icon)
italic_btn = ttk.Button(tool_bar, image=italic_icon)
underlined_btn = ttk.Button(tool_bar, image=underlined_icon)
color_btn = ttk.Button(tool_bar, image=color_icon)
left_btn = ttk.Button(tool_bar, image=left_icon)
centre_btn = ttk.Button(tool_bar, image=centre_icon)
right_btn = ttk.Button(tool_bar, image=right_icon)
# justify_btn = ttk.Button(tool_bar, image=justify_icon)

# button grids

bold_btn.grid(row=0, column=2, padx=5)
italic_btn.grid(row=0, column=3, padx=5)
underlined_btn.grid(row=0, column=4, padx=5)
color_btn.grid(row=0, column=5, padx=5)
left_btn.grid(row=0, column=6, padx=5)
centre_btn.grid(row=0, column=7, padx=5)
right_btn.grid(row=0, column=8, padx=5)
# justify_btn.grid(row=0, column=9, padx=5)


#***************************************** end tool Bar *********************************



# ************************************** Text Editor ***********************************

text_editor = tk.Text(window)
text_editor.config(wrap="word", relief=tk.FLAT)

scroll_bar = tk.Scrollbar(window)
text_editor.focus_set()

scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)

scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# ****************************************** text editor functionability **************************************
current_fammily = "Arial"
current_size = 10



def change_family(event=None):
    global current_fammily
    current_fammily = font_family.get()
    text_editor.config(font=(current_fammily, current_size))

def change_size(event = None):
    global current_size
    current_size = size_var.get()
    text_editor.config(font=(current_fammily, current_size))

font_box.bind("<<ComboboxSelected>>", change_family)
size_box.bind("<<ComboboxSelected>>", change_size)

text_editor.config(font=('Arial', 10))
# bold button

def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()["weight"] == "normal":
        text_editor.config(font=(current_fammily, current_size, "bold"))
    if text_property.actual()["weight"] == "bold":
        text_editor.config(font=(current_fammily, current_size, "normal"))

bold_btn.config(command=change_bold)
        
# print(tk.font.Font(font=text_editor['font']).actual())

def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()["slant"] == "roman":
        text_editor.config(font=(current_fammily, current_size, "italic"))
    if text_property.actual()["slant"] == "italic":
        text_editor.config(font=(current_fammily, current_size, "roman"))

italic_btn.config(command=change_italic)


# underline button

def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()["underline"] == 0:
        text_editor.config(font=(current_fammily, current_size, "underline"))
    if text_property.actual()["underline"] == 1:
        text_editor.config(font=(current_fammily, current_size, "normal"))

underlined_btn.configure(command=change_underline)


# color button

def change_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.config(fg=color_var[1]) # if you print color_var you will get a tuple with rgb and hexa values in 0 and 1 position

color_btn.config(command=change_color)


# text alignment

def left_aligment():
    text_content = text_editor.get(1.0,"end")
    text_editor.tag_config("left", justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "left")

left_btn.config(command=left_aligment)

def center_aligment():
    text_content = text_editor.get(1.0,"end")
    text_editor.tag_config("center", justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "center")

centre_btn.config(command=center_aligment)

def right_aligment():
    text_content = text_editor.get(1.0,"end")
    text_editor.tag_config("right", justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "right")

right_btn.config(command=right_aligment)



#************************************** text editor end ************************************



# *************************************** Status Bar ************************************
staus_bar = tk.Label(window, text="Status")
staus_bar.pack(side=tk.BOTTOM, fill=tk.X)

# status bar fuctionability
text_changed = False
def status(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0,"end-1c").split())
        characters = len(text_editor.get(1.0,"end-1c").replace(" ",""))
        staus_bar.config(text=f"Characters:{characters} | Words:{words}")
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>", status)

# ************************************ End status bar *********************************

# ************************************exit funtion*****************************
def exit_file(event = None):
    global url, text_changed
    try:
        if text_changed:
            message = m_box.askyesnocancel("Warning","Do you want to save this file?")
            if message is True:
                if url:
                    content = str(text_editor.get(1.0,tk.END))
                    with open(url,"w", encoding="UTF-8") as wf:
                        wf.write(content)
                        window.destroy()
                else:
                    url = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=(('text files', '*.txt'),('all files','*.*')))
                    content2 = str(text_editor.get(1.0,tk.END))
                    url.write(content2)
                    url.close()
                    window.destroy()
            elif message is False:
                window.destroy()
        else:
            window.destroy()
    except:
        return
    
# exit command
file_menu.add_command(label="Exit", image=exit_icon, compound=tk.LEFT, command=exit_file, accelerator="Ctrl+Q")

#*************************************binding with shortcut keys***********************

window.bind("<Control-n>", new_file)
window.bind("<Control-o>", open_file)
window.bind("<Control-s>", save_file)
window.bind("<Control-e>", save_as)
window.bind("<Control-q>", exit_file)
window.bind("<Control-r>", clear_text)
window.bind("<Control-f>", find_content)
window.bind("<Control-t>", hide_toolbar)
window.bind("<Control-Alt-s>", hide_statusbar)


window.config(menu=main_menu)
window.mainloop()