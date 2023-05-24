from turtle import Turtle, Screen
import random, time

my_screen = Screen()
my_screen.setup(width=800, height=700)
my_screen.title('Bet your Turtle')


arrow = Turtle()
arrow.penup()
arrow.goto(-360,-230)
arrow.setheading(90)
arrow.pendown()
arrow.forward(420)
arrow.setheading(0)
arrow.penup()
arrow.forward(740)
arrow.setheading(270)
arrow.pendown()
arrow.forward(420)


deku = Turtle(shape='turtle')
ochako = Turtle(shape='turtle')
lida = Turtle(shape='turtle')
shoto = Turtle(shape='turtle')
bakugo = Turtle(shape='turtle')
kirishima = Turtle(shape='turtle')

racers = [deku,ochako,lida,shoto,bakugo,kirishima]
colors = ['green','pink','blue','indigo','orange','red']


while True:
    user_bet = my_screen.textinput(title='Bet your winner', prompt="'green','pink','blue','indigo','orange' and 'red' who will win? ").strip()
    race_starts = False
    height = -220
    for i in range(6):
        racers[i].penup()
        racers[i].color(colors[i])
        racers[i].goto(-370, height)
        height += 80

    if user_bet:
        race_starts =True

    time.sleep(3)

    while race_starts:
        for people in racers:
            people.forward(random.randint(1,10))
            if people.xcor() > 370:
                race_starts = False
                winning_color = people.pencolor()
                if winning_color == user_bet:
                    print(f'you won the bet.{user_bet} has won the race')
                else:
                    print(f'you lost.{winning_color} has won the race')
                
    user_choice = my_screen.textinput(title='Restart', prompt='Wanna bet again? \'Yes\' or \'No\' ').lower().strip()
    if user_choice == 'yes':
        continue
    else:
        my_screen.bye()
        break

    





my_screen.mainloop()