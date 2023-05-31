from turtle import Turtle

class Making_Turtle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x,y)

    def write_name(self,name):
        self.pendown()
        self.write(name, False, "center", ("Arial",10,"normal"))
        self.penup()
