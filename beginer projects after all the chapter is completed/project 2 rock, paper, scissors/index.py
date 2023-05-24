import random

def play():
    user = input("What's your choice? press \'r\' for rock, \'p\' for paper and \'s\' for scissors\n").lower()
    computer = random.choice(['r','p','s'])

    if user == computer:
        return print(f"it's a tie. my choice was also {computer}")
    elif is_win(user,computer):
        return print(f"Damn!you win. my choice was {computer}")
    return print(f"yay!you lost. my choice was {computer}")

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

play()