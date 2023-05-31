import turtle, pandas
from turtle_class import Making_Turtle

screen = turtle.Screen()
image = "img.gif"
screen.addshape(image)
turtle.shape(image)


all_data = pandas.read_csv("states_data.csv")
state_names = all_data.state.to_list()


user_guess = 0
while user_guess < 50:
    user_ans = screen.textinput(f"{user_guess}/50 Guess a state", "what is your guess?").title().strip()
    if user_ans in state_names:
        name_row = all_data[all_data.state == user_ans]
        writing_turtle = Making_Turtle(int(name_row.x), int(name_row.y))
        writing_turtle.write_name(user_ans)
        user_guess += 1
    elif user_ans == "Exit":
        break
    