import tkinter as tk
import random
from tkinter import messagebox
import pandas

BACKGROUND_COLOR = "#B1DDC6"
word = {}
list_dict_words = {}

try:
    data_other = pandas.read_csv("to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    list_dict_words = original_data.to_dict(orient="records")
else:
    list_dict_words = data_other.to_dict(orient="records")




# print(list_dict_words)

########################################### FUNCTIONALITY ################################################

def word_change():
    global flip_timer, word
    window.after_cancel(flip_timer)
    word = random.choice(list_dict_words)
    canvas.itemconfig(title_text, text = "French", fill = "black")
    canvas.itemconfig(word_text, fill = "black")
    canvas.itemconfig(canvas_background, image = canvas_image_fnt)
    canvas.itemconfig(word_text, text = word["French"])
    flip_timer = window.after(3000, flip_card)
    # print(WORD)


def flip_card():
    canvas.itemconfig(title_text, text = "English", fill = "white")
    canvas.itemconfig(word_text, fill = "white")
    canvas.itemconfig(canvas_background, image = canvas_image_bg)
    canvas.itemconfig(word_text, text = word["English"])


def right():
    list_dict_words.remove(word)
    data = pandas.DataFrame(list_dict_words)
    data.to_csv("to_learn.csv", index=False)
    word_change()



window = tk.Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)
canvas = tk.Canvas(window, width=800, height= 526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image_bg = tk.PhotoImage(file="card_back.png")
canvas_image_fnt = tk.PhotoImage(file="card_front.png")
canvas_background = canvas.create_image(400,263, image = canvas_image_bg)
title_text = canvas.create_text(400, 140, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

word_change()


r8_image = tk.PhotoImage(file="right.png")
r8_button = tk.Button(window,image=r8_image, bg=BACKGROUND_COLOR, highlightthickness=0, command= right)
r8_button.grid(column=0, row=1)


wrong_image = tk.PhotoImage(file="wrong.png")
wrong_button = tk.Button(window, image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command= word_change)
wrong_button.grid(column=1, row=1)






window.mainloop()
