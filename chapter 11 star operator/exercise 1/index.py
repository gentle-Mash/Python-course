power = int(input("enter your power "))
list_range = input("enter how many numbers you want to power up from 1 to 100 ")

if list_range == "":
    args = []
else:
    args = [i for i in range(1, int(list_range)+1)]

def power_up(num, *args):
    if args:
       return [i**num for i in args]
    else:
        return "you didn't pass any arguement"

print(power_up(power, *args))
