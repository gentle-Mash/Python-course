give_numb = input("enter more than 1 digit number ")

total = 0
i = 0 
while i < len(give_numb):
    total += int(give_numb[i])
    i += 1
print(f"your total is {total}")  