import random

words = ['apple', 'banana', 'mango', 'jack-fruit', 'manderine', 'absent', 'abuse', 'good', 'bad', 'great', 'right',
         'wrong', 'up', 'down', 'left', 'quick', 'first', 'fast', 'slow', 'seco-nd', 'third', 'cat', 'dog', 'snake',
         'camel', 'tiger', 'fox', 'wolf', 'river', 'ocean', 'asia', 'bangladesh', 'japan', 'pacific', 'liter ature',
         'science', 'biology', 'physics', 'football']


def get_valid_word(words):
    word = random.choice(words)
    while ('-' in word) or (' ' in word):
        word = random.choice(words)
    return word


lives = 7


def hangman():
    global lives

    word = get_valid_word(words)
    word = word.upper()

    # print(word)
    right_word = ["_" for i in range(len(word))]
    # print(f"the word is {right_word}")

    word_letters = list(word)
    used_letters = list()

    while len(word_letters) > 0 and lives > 0:

        print(f"Guess the word {right_word}    lives = {lives}")

        user_letter = input("Guess a letter: ").upper()
        if (user_letter in word_letters) and (user_letter not in used_letters):
            used_letters.append(user_letter)
            indices = [i for i, letter in enumerate(word) if letter == user_letter]
            for index in indices:
                word_letters.remove(user_letter)
                right_word[index] = user_letter
        elif (user_letter in used_letters) and (user_letter in word):
            print("you have already guessed it. try different letter")
        else:
            lives -= 1
            print(f"you guessed wrong. guess again. your remaining live is {lives}")

    if len(word_letters) == 0:
        print(f"yay!! you guessed the right word {right_word} : {word}")
    elif lives == 0:
        print(f"Sorry. you lost!!! the word was {word}")


hangman()
