
square = {num:num**2 for num in range(1,11)}
print(square)
for i, j in square.items():
    print(f"square of {i} is {j}")

string = "Ochako"
coun = {char:string.count(char) for char in string}
print(coun)