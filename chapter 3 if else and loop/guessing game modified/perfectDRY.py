import random
random_number = random.randint(1,100)
user_numb = int(input("guess any number between 1 to 100 ").strip())

guessing_times = 1
game_over = False


while not game_over:
    if user_numb == random_number:
        if guessing_times > 1:
            print(f"you win! and you guessed this number in {guessing_times} times")
            game_over = True
        elif guessing_times == 1:
            print(f"you win! and you guessed this number in {guessing_times} time")
            game_over = True
    else:
        if user_numb > random_number:
            print("wrong guess.your number is higher ")
        else:
            print("wrong guess.your number is lower ")
        guessing_times += 1
        user_numb = int(input("guess again "))   