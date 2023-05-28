from turtle import Turtle
STARTING_POSITION = [(0,0),(-10,0),(-20,0)]
MOVE_DISTANCE = 10
class Snake:
    def __init__(self):
        self.main_body = []
        for position in STARTING_POSITION:
            self.add_body(position)
        self.head = self.main_body[0]

    def add_body(self, position):
        snake_body = Turtle(shape='square')
        snake_body.shapesize(stretch_len=0.5, stretch_wid=0.5)
        snake_body.penup()
        snake_body.color('black')
        snake_body.goto(position)
        self.main_body.append(snake_body)

    def extend(self):
        self.add_body(self.main_body[-1].position())

    def move(self):
            for step in range(len(self.main_body)-1, 0, -1):
                x = self.main_body[step - 1].xcor()
                y = self.main_body[step - 1].ycor()
                self.main_body[step].goto(x,y)
            self.main_body[0].forward(MOVE_DISTANCE)

    def restart(self):
        for body in self.main_body:
            body.goto(700,700)
        self.main_body.clear()
        
        for position in STARTING_POSITION:
            self.add_body(position)
        self.head = self.main_body[0]
        

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)