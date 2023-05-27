from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.left(30)
        self.penup()
        self.speed("fastest")
        self.x_move = 10
        self.y_move = 10
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def change_direction_y(self):
        self.y_move *= -1
    
    def change_direction_x(self):
        self.x_move *= -1
