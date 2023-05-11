user_number =    input("enter any number including more than 1 digit ")

total = 0
for i in range(len(user_number)):
    total += int(user_number[i])
print(total)