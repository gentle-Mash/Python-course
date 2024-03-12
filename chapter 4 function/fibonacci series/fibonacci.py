n = int(input("enter the length you want of Fibonacci series "))

def new_input():
    new = int(input("enter again "))
    return fibonacci(new)

def fibonacci(n):
    if n <= 0:
        print("please enter a number that is greater than 0 ")
        new_input()
        return
    fibonacci_previous = 0
    fibonacci_current = 1

    if n == 1:
        print(fibonacci_previous)
    elif n == 2:
        print(f"{fibonacci_previous}, {fibonacci_current}")
    else:
        print(f"{fibonacci_previous}, {fibonacci_current}", end = ", ")
        for i in range(n-2):
            fibonacci_new = fibonacci_previous + fibonacci_current
            fibonacci_previous = fibonacci_current
            fibonacci_current = fibonacci_new
            print(fibonacci_current, end=", ")
    # print()

fibonacci(n)

    
        