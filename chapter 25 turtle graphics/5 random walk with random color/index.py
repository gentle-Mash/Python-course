from turtle import Turtle, Screen, colormode
import random

colormode(255)
directions = [0,90,180,270]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    colors = (r,g,b)
    return colors

arrow = Turtle()
arrow.pensize(10) # you can also use width() method
arrow.speed('fastest')


for i in range(200):
    arrow.color(random_color())
    arrow.forward(30)
    arrow.setheading(random.choice(directions))

    

my_screen = Screen()
my_screen.exitonclick()