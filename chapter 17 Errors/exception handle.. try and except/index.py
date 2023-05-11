i = 0
while True:
    try:
        if i == 0:
            age = int(input("enter your age "))
        else:
            age = int(input("enter your age again "))
        break
    except ValueError: # in case you know the upcoming error in your try block
        print("you have inputed string. please input int data type")
        i += 1
    except: # for any kind of error
        print("unexpected error")
        i += 1

if age >= 18:
    print("you can play this game")
else:
    print("you can't play this game")