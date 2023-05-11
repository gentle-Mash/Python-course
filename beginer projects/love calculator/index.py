user_name = input("Enter your name: ").lower().strip()
lovers_name = input("Enter your lover's name: ").lower().strip()

for char in user_name:
    if char in "true":
        print(f"{char} is {user_name.count(char)} times")

for char in lovers_name:
    if char in "love":
        print(f"{char} is {lovers_name.count(char)} times")


