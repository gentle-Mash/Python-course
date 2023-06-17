import random

LETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

NUMBERS = ['0','1','2','3','4','5','6','7','8','9']

SYMBOLES = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+',',','<','.','>','/','?','\\','|','\"','\'']


def generate():
    user_letter = random.randint(3,11)
    user_number = random.randint(3,5)
    user_symbol = random.randint(3,5)
    password = []

    letter_list = [random.choice(LETTERS) for i in range(user_letter)]
    number_list = [random.choice(NUMBERS) for i in range(user_number)]
    symbol_list = [random.choice(SYMBOLES) for i in range(user_symbol)]
    
    password = letter_list + number_list + symbol_list
    random.shuffle(password)

    new_pass = "".join(password)

    return new_pass



