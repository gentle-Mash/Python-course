user_name = input("Enter your name: ").lower().strip()
lovers_name = input("Enter your lover's name: ").lower().strip()

print(f"in {user_name}:\nthe number of \'t\' is {user_name.count('t')}")
print(f"the number of \'r\' is {user_name.count('r')}")
print(f"the number of \'u\' is {user_name.count('u')}")
print(f"the number of \'e\' is {user_name.count('e')}")

print(f"in {lovers_name}:\nthe number of \'l\' is {lovers_name.count('l')}")
print(f"the number of \'o\' is {lovers_name.count('o')}")
print(f"the number of \'v\' is {lovers_name.count('v')}")
print(f"the number of \'e\' is {lovers_name.count('e')}")

total_user_num = user_name.count('t') + user_name.count('r') + user_name.count('u') + user_name.count('e')

total_lovers_num = lovers_name.count('l') + lovers_name.count('o') + lovers_name.count('v') + lovers_name.count('e')


print("so your love chemistry with your lover is " + str(total_user_num) + str(total_lovers_num) + "%")

percentage = int(str(total_user_num) + str(total_lovers_num))

if 20 < percentage <= 50:
    print("you two are okay")
elif percentage > 50 and percentage < 90:
    print("you two are so good")
else:
    print("IDK")