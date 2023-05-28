from turtle import Turtle
import random
COLORS = ['red','green','blue','orange','pink','brown']

class Cars:
    def __init__(self):
        self.all_cars = []
        self.MOVE_DISTANCE = 3

    def create_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-260,260)
            new_car.goto(400,random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.MOVE_DISTANCE)

    def game_over(self):
        write = Turtle()
        write.hideturtle()
        write.penup()
        write.write("Game Over", False, "center", ("Courier", 15, "normal"))

    def speed_up(self):
        self.MOVE_DISTANCE += 3

