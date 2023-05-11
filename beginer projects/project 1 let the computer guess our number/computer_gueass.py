import random

def computer_guess(x):
    low = 0
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low = high
        feedback = input(f"is my guess {guess} is too high (H) or too low (L) or correct (C)?  ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"yay!! I guessed the right number {guess}")

input_number = int(input("tell the range of your number from 0 to "))

computer_guess(input_number)

