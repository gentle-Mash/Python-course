from turtle import Turtle, Screen
import random, time, os, turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.title('Snaky Snake')
screen.setup(600,600)
screen.bgcolor('white')
screen.tracer(0)

body = Snake()
snacks = Food()
score = Scoreboard()

def gameplay():
    screen.listen()
    screen.onkey(body.up,'Up')
    screen.onkey(body.down,'Down')
    screen.onkey(body.right,'Right')
    screen.onkey(body.left,'Left')

    play_game = True
    while play_game:
        screen.update()
        time.sleep(0.06)
        body.move()


        # detect collision with food
        if body.head.distance(snacks) < 10:
            snacks.refresh()
            score.increase_score()
            body.extend()


        #detect collision with wall
        if body.head.xcor() > 295 or body.head.xcor() < -295 or body.head.ycor() > 295 or body.head.ycor() < -295:
            play_game = False
            score.game_over()
            if score.score > score.high_score:
                with open("data.txt","w") as DATA:
                    DATA.write(str(score.score))
                score.read_high_score()
            play_again()

        # detect colision with tail
        for snake in body.main_body[1:]:
            if body.head.distance(snake) < 5:
                play_game = False
                score.game_over()
                play_again()


def play_again():
    user_input = turtle.textinput(title="Play again?", prompt="Type \'Yes\' or \'No\' ").lower().strip()
    if user_input == "yes":
        score.read_high_score()
        body.restart()
        score.restart()
        time.sleep(3)
        gameplay()
    else:
        screen.bye()  


gameplay()                


screen.mainloop()