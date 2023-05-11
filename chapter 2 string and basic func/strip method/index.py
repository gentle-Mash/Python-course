name = "      harshit vashistha     "
dots = ".................."

print(name.lstrip() + dots)
print(name.rstrip() + dots)
print(name.strip() + dots)
print(name.replace(" ", "") + dots)

#exercise 3 debugging

user_name, char = input("please input your name and the character you want to count \'please seperate them with comma\' ").split(",");
print(f"the length of your name is {len(user_name.strip())}");
print(f"the number of {char} is {user_name.lower().count(char.lower().strip())}");