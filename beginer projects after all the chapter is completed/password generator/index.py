import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+',',','<','.','>','/','?','\\','|','\"','\'']

user_letter = int(input("how many latters you want to use in your passord? ").strip())
user_number = int(input("how many numbers you want to use in your passord? ").strip())
user_symbol = int(input("how many symbols you want to use in your passord? ").strip())

password = ""

# letter_chose = []
for i in range(user_letter):
    password += random.choice(letters)

# number_chose = []
for i in range(user_number):
    password += random.choice(numbers)

# symbol_chose = []
for i in range(user_symbol):
    password += random.choice(symbols)

# all_char = [letter_chose,number_chose,symbol_chose]
# full_pass = []
# for char in all_char:
#     full_pass.extend(char)

# print(full_pass)

# password = ""

# for i in range(len(full_pass)):
#     password += full_pass[i] 

# print(f"your password is {password}")

unshuffle = []
for char in password:
    unshuffle += char

# print(unshuffle)

random.shuffle(unshuffle)

# print(unshuffle)

new_pass = ""
for char in unshuffle:
    new_pass += char

print(f"your password is {new_pass}")


