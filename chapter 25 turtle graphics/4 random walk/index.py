from turtle import Turtle, Screen
import random

colors = ['cyan','green yellow','slate gray','orange','red','violet']
directions = [0,90,180,270]

arrow = Turtle()
arrow.pensize(7) # you can also use width() method
arrow.speed('fast')

my_screen = Screen()
for i in range(200):
    arrow.color(random.choice(colors))
    arrow.forward(50)
    arrow.setheading(random.choice(directions))

    

# my_screen.setworldcoordinates(-300,-300,300,300)
my_screen.exitonclick()