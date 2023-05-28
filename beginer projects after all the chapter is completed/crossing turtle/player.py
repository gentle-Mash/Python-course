from turtle import Turtle

class Player(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(x,y)
        self.setheading(90)

    def move(self):
        self.forward(20)