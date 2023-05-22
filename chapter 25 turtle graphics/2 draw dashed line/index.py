from turtle import Turtle, Screen

tim = Turtle()

for i in range(10):
    tim.fd(10)
    tim.penup()
    tim.fd(10)
    tim.pendown()



Screen().exitonclick()