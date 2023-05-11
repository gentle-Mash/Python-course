import random

random_number = random.randint(0,10)
user_number = int(input("guess a number "))

if user_number == random_number:
    print("you win!!!")
elif user_number > random_number:
    print(f"you lost. your number is higher. \nwinning number is {random_number}")
elif user_number < random_number:
    print(f"you lost. your number is lower. \nwinning number is {random_number}")

