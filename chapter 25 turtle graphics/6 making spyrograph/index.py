from turtle import Turtle, Screen, colormode
import random

colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

spyrograph = Turtle()
spyrograph.speed('fastest')
# current_heading = spyrograph.heading()
def draw_spyrograph(gap_size):

    for i in range(360 // gap_size):
        spyrograph.color(random_color())
        spyrograph.circle(100)
        spyrograph.setheading(spyrograph.heading() + gap_size)

draw_spyrograph(3)
    
    
    


Screen().exitonclick()