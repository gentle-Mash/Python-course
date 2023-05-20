from datas import data
import random

choice1 = random.choice(data)
choice2 = random.choice(data)

while choice1 == choice2:
    choice2 = random.choice(data)

choices = [choice1,choice2]

def compete(choice1, choice2):
    print(f"Who has more follower? ||||| points:{points}")
    print(choice1['name']+' VS '+ choice2['name'])
    user_guess = input("Higher or Lower?\n").lower().strip()
    if user_guess == "higher":
        user_guess = True
    else:
        user_guess = False

    user_win_or_lose = choice1['follower_count'] > choice2['follower_count']
    if user_guess == user_win_or_lose:
        user_win_or_lose = True
    else:
        user_win_or_lose = False
    return user_win_or_lose

points = 0
win = True
while win:
    user_win_or_lose = compete(choice1,choice2)
    if user_win_or_lose:
        another_choice = random.choice(data)
        while another_choice in choices:
            another_choice = random.choice(data)

        choices.append(another_choice)
        if choice1['follower_count'] > choice2['follower_count']:
            choice2 = another_choice
        elif choice1['follower_count'] < choice2['follower_count']:
            choice1 = choice2
            choice2 = another_choice
        points += 1
    else:
        print(f"Game over.your points {points}")
        win = False
        



