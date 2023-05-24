# import colorgram

# collecting color using colorgram

# colors = colorgram.extract('lion.jpg',30)
# color_plate = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r,g,b)
#     color_plate.append(rgb)

# print(color_plate)

import random
import turtle as t
from turtle import Screen

t.colormode(255)

color_list = [(25, 104, 172), (23, 31, 44), (208, 29, 65), (232, 224, 203), (215, 132, 161), (214, 152, 116), (225, 212, 62), (217, 70, 121), (51, 23, 32), (180, 24, 37), (36, 162, 197), (185, 55, 35), (50, 169, 158), (229, 173, 169), (223, 89, 74), (38, 129, 108), (48, 32, 23), (138, 182, 163), (24, 39, 35), (98, 171, 193), (190, 152, 44), (230, 165, 174), (149, 29, 26), (22, 90, 75), (105, 119, 167), (228, 210, 214), (217, 223, 220), (21, 81, 96), (170, 202, 186)]

timmy = t.Turtle()
timmy.speed('fastest')
timmy.hideturtle()
timmy.penup()
timmy.goto(-240,-230)

y = -230
for i in range(10):
    for i in range (10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)
    y += 50
    timmy.goto(-240, y)







Screen().mainloop()


