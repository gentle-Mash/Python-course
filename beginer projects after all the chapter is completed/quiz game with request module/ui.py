THEME_COLOR = "#375362"

import tkinter as tk
from BrainQuiz import BrainQuiz


class Interface():
    def __init__(self, quiz_obj:BrainQuiz):
        self.quizz = quiz_obj
        self.window = tk.Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR, padx=20,pady=20)

        self.score = tk.Label(self.window, text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial",12,"bold"))
        self.score.grid(row=0, column=1,sticky=tk.E)

        self.canvas = tk.Canvas(self.window, width=300, height=250, bg= "white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.que_text = self.canvas.create_text(150,125, text="Some text here", font=("Arial",20,"italic"), fill=THEME_COLOR, width=280)

        true_image = tk.PhotoImage(file="true.png")
        false_image = tk.PhotoImage(file="false.png")

        self.true_button = tk.Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_button = tk.Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        self.next_que()

        self.window.mainloop()

    def next_que(self):
        self.canvas.config(bg="white")
        if self.quizz.que_left():
            self.score.config(text=f"Score: {self.quizz.score}")
            que = self.quizz.next_que()
            self.canvas.itemconfig(self.que_text, text = que)
        else:
            self.canvas.itemconfig(self.que_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quizz.check_ans("true")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quizz.check_ans("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000, self.next_que)




