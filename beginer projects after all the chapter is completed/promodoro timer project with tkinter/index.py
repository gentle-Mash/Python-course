import tkinter as tk
from tkinter import ttk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repeat = 0
time = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global repeat
    repeat = 0
    window.after_cancel(time)
    canvas.itemconfig(timer, text = "00:00")
    timer_label.config(text="Timer", foreground=GREEN)
    check_mark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global repeat
    repeat += 1
    working = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60

    
    if repeat % 8 == 0:
        timer_label.config(text="Break", foreground=RED)
        counter(long_break)
    elif repeat % 2 == 0:
        timer_label.config(text="Break", foreground=PINK)
        counter(short_break)
    else:
        timer_label.config(text="Work", foreground=GREEN)
        counter(working)

    # counter(WORK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def counter(count):
    count_min = math.floor(count/60)
    count_seconds = count % 60

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer, text = f"{count_min}:{count_seconds}")
    if count>0:
        global time
        time = window.after(1000, counter, count-1)
    else:
        start_timer()
        mark = ""
        if repeat % 2 == 0:
            for i in range(repeat//2):
                mark += "✓"
            check_mark_label.config(text=mark)
        


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Promodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = tk.Canvas(window, width=200, height=224, highlightthickness=0, bg= YELLOW)
image_png = tk.PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=image_png) #this coordinates don't work like typical co ordinates from 0,0 center. it's 0,0 starts from upper left corner
timer = canvas.create_text(100,140, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)


timer_label = ttk.Label(window, text="Timer", font=(FONT_NAME, 45), foreground=GREEN, background=YELLOW)
timer_label.grid(column=1, row=0)


start_the_timer = ttk.Button(window, text="Start", command=start_timer)
start_the_timer.grid(column=0, row=2)


reset_the_timer = ttk.Button(window, text="Reset", command=reset_timer)
reset_the_timer.grid(column=2, row=2)


check_mark_label = ttk.Label(window, font=(FONT_NAME, 18, "bold"), foreground=GREEN, background=YELLOW)
check_mark_label.grid(column=1, row=3)



for child in window.winfo_children():
    child.grid_configure(pady=5)


window.mainloop()