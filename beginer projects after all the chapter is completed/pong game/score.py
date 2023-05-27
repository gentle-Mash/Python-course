from turtle import Turtle

class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x,y)
        self.write(f"{self.score}", False, "right", ("Courier", 45, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", False, "center", ("Courier", 45, "normal"))

