from turtle import Turtle
FONT = "Arial"
ALIGNMENT = "center"
FONT_SIZE = 15


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt","r") as DATA:
            self.high_score = int(DATA.read())
        self.color('black')
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score} || High Score: {self.high_score} ", False, ALIGNMENT, (FONT, FONT_SIZE, "bold"))
        self.hideturtle()
    
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} || High Score: {self.high_score} ", False, ALIGNMENT, (FONT, FONT_SIZE, "bold"))

    def read_high_score(self):
        with open("data.txt","r") as DATA:
            self.high_score = int(DATA.read())

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", False, ALIGNMENT, (FONT, FONT_SIZE, "bold"))

    def restart(self):
        self.clear()
        self.score = 0
        self.goto(0,270)
        self.write(f"Score: {self.score} || High Score: {self.high_score}", False, ALIGNMENT, (FONT, FONT_SIZE, "bold"))
        

