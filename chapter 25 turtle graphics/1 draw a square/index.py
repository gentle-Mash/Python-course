from turtle import Turtle , Screen


my_turtle = Turtle()
my_turtle.shape("turtle")

my_turtle.fd(100)
my_turtle.left(90)
my_turtle.fd(100)
my_turtle.left(90)
my_turtle.fd(100)
my_turtle.left(90)
my_turtle.fd(100)
my_turtle.left(90)


# instead of these many lines of code, you could also code like this

# for i in range(4):
#     my_turtle.fd(100)
#     my_turtle.left(90)

# my_screen = Screen()
Screen().exitonclick()