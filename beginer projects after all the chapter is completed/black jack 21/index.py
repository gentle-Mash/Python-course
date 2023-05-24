import random


def main():
    numbers = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "king", "queen", "joker"]

    def making_list():
        return [(random.choice(numbers)) for i in range(2)]

    user = making_list()
    origin_user = user.copy()

    computer = making_list()
    origin_computer = computer.copy()

    fake_computer = []
    fake_computer.append(computer[0])
    for i in range(len(computer)-1):
        fake_computer.append("_")

    print(f"your cards: {origin_user} || computer cards: {fake_computer}")

# turning special cards into inteser
    for i in range(len(user)):
        if (user[i] == "king") or (user[i] == "queen") or (user[i] == "joker"):
            user[i] = 10
    for i in range(len(computer)):
        if (computer[i] == "king") or (computer[i] == "queen") or (computer[i] == "joker"):
            computer[i] = 10

    def user_total_func():  # calculting the total of user cards with ace fact 
        while True:
            user_total = 0
            for item in user:
                if item == "ace":
                    continue
                user_total += item

            if "ace" in user and user_total <= 10:
                user[user.index("ace")] = 11
            elif "ace" in user and user_total > 10:
                user[user.index("ace")] = 1
            else:
                break
        return user_total

    def computer_total_func(): # calculting the total of computer cards with ace fact 
        while True:
            computer_total = 0
            for item in computer:
                if item == "ace":
                    continue
                computer_total += item    

            if "ace" in computer and computer_total <= 10:
                computer[computer.index("ace")] = 11
            elif "ace" in computer and computer_total > 10:
                computer[computer.index("ace")] = 1
            else:
                break   
        return computer_total

    user_total = user_total_func() 
    computer_total = computer_total_func()

    if computer_total < 17:
        computer.append(random.choice(numbers))
        origin_computer.append(computer[-1])   
        for i in range(len(computer)):
            if (computer[i] == "king") or (computer[i] == "queen") or (computer[i] == "joker"):
                computer[i] = 10
        computer_total = computer_total_func()

    hit = input("if you wnat to hit type \'hit\' or if you want to stand type \'stand\'\n").strip()

    def result(): # the result function
        if user_total < 22 and user_total > computer_total:
            print(f"you win. computer cards were {origin_computer}")
        elif computer_total > 21 and user_total < 22:
            print(f"you win. computer is busted. computer cards were {origin_computer}")
        elif computer_total == user_total and computer_total < 22 and user_total < 22:
            print(f"it's a draw. computer cards were {origin_computer}")
        elif computer_total > 21 and user_total > 21:
            print(f"it's a draw. Both you and computer are busted up. computer cards were {origin_computer}")
        else:
            print(f"you busted up. computer cards were {origin_computer}")
        play_again = input("wanna play again? type \'yes\' or \'no\'\n").strip()
        if play_again == "yes":
            main()
        else:
            print("thanks for playing.please come again.")

    if hit == "hit":
        while user_total < 21:
            user.append(random.choice(numbers))
            origin_user.append(user[-1])
            for i in range(len(user)):
                if (user[i] == "king") or (user[i] == "queen") or (user[i] == "joker"):
                    user[i] = 10
            user_total = user_total_func()

            print(f"your cards {origin_user}")
            hit_again = input("if you want to hit again type \'hit\' otherwise type \'no\'\n").strip()
            if hit_again == "hit":
                continue
            else:
                break
        result()
    else:
        result()
    
play = input("Welcome to BlackJack 21. Wanna play? type \'yes\' or \'no\' ").strip().lower()
if play == "yes":
    main()
else:
    print("Goodbye")