i = 0
while True:
    try:
        if i == 0:
            age = int(input("enter your age "))
        else:
            age = int(input("enter your age again "))
    except ValueError: # in case you know the upcoming error in your try block
        print("you have inputed string. please input int data type")
        i += 1
    except: # for any kind of error
        print("unexpected error")
        i += 1
    else: # when no exception or error is occured else block will be wxecuted after try block. So you should not write everything in try block
        print(f"user input {age}") # instead you should write just the portion where error can be occured in your try block and the remains should be in else block
        break
    finally: # this block doesn't care if there is error or not . in both cases finally block will be executed anyway
        print("No more codes")

if age >= 18:
    print("you can play this game")
else:
    print("you can't play this game")