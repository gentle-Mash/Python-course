from turtle import Turtle, Screen


colors = ['black','red','green','blue','orange','indigo','purple','brown']
arrow = Turtle()
arrow.penup()
arrow.goto(0,120)
arrow.pendown()


j = 3
for i in range(7):
    arrow.color(colors[i])
    for i in range(j):
        arrow.right(360/j)
        arrow.fd(100)
    j += 1
        
Screen().exitonclick()