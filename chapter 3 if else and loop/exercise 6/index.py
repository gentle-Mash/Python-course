user_numbers = input("enter student's numbers seperated by comma: ").strip().split(",")

for i in range(len(user_numbers)):
    user_numbers[i] = int(user_numbers[i])

highest_score = 0
for number in user_numbers:
    if number > highest_score:
        highest_score = number
print(f"the highest score is {highest_score}")
