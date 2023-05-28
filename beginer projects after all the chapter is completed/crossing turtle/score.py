from turtle import Turtle

class Score(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x,y)
        self.write(f"Level: {self.level}", False, "center", ("Courier", 25, "normal"))

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, "center", ("Courier", 25, "normal"))

        