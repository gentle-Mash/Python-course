from turtle import Turtle, Screen
import turtle, random, time
from paddle import Paddle
from ball import Ball
from score import Score

SPEED = 0.1

screen = Screen()
screen.title("Pong")
screen.setup(width=1000, height=600)
screen.tracer(0)

paddle1 = Paddle(450,0)
paddle2 = Paddle(-450,0)
ball = Ball()
score1 = Score(100,230)
score2 = Score(-70,230)



def midline():
    arrow = Turtle()
    arrow.penup()
    arrow.goto(0,293)
    arrow.pensize(5)
    
    arrow.setheading(270)
    for i in range(15):
        arrow.pendown()
        arrow.forward(20)
        arrow.penup()
        arrow.forward(20)
    arrow.hideturtle()

midline()


screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")


game_started = True
while game_started:
    time.sleep(SPEED)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.change_direction_y()

    #detect collision with paddle
    if (ball.xcor() == 430  and ball.distance(paddle1) < 56) or (ball.xcor() == -430  and ball.distance(paddle2) < 56):
        if SPEED > 0.03:
            SPEED -= 0.003
        ball.change_direction_x()
    
    #what happens if paddle misses the ball
    if ball.xcor() > 500:
        score2.update_score()
        SPEED = 0.1
        ball.goto(0,0)
    elif ball.xcor() < -500:
        score1.update_score()
        SPEED = 0.1
        ball.goto(0,0)

  




















screen.mainloop()