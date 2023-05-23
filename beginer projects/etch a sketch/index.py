from turtle import Turtle, Screen, listen

tim = Turtle()
screen = Screen()
screen.listen()

def move_forward():
    tim.forward(15)
def move_backwards():
    tim.backward(15)
def clockwise():
    tim.right(5)
def counter_clockwise():
    tim.left(5)
def circle():
    tim.circle(100)
def clear():
    tim.clear()
def home():
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(key='w', fun= move_forward)
screen.onkey(key='s', fun= move_backwards)
screen.onkey(key='d', fun= clockwise)
screen.onkey(key='a', fun= counter_clockwise)
screen.onkey(key='o', fun= circle)
screen.onkey(key='h', fun= home)
screen.onkey(key='c', fun= clear)


screen.mainloop()