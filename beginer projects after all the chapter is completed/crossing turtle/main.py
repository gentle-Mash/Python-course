import time
from turtle import Screen
from player import Player
from cars import Cars
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

timmy = Player(0,-280)
my_cars = Cars()
level = Score(-300, 250)


screen.listen()
screen.onkey(timmy.move, "Up")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    my_cars.create_car()
    my_cars.move()

    for car in my_cars.all_cars:
        if timmy.distance(car) < 20:
            game_on = False
            my_cars.game_over()
            

    if timmy.ycor() == 300:
        level.level_up()
        timmy.goto(0, -280)
        my_cars.speed_up()



screen.mainloop()
