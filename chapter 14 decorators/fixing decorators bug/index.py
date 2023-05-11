# def decorator(any_function):
#     def wrapper():
#         print("I'm enhancing your function")
#         any_function()
#     return wrapper

# problem 1
# if you c=use decorators with a function that takes arguements
# your decorator won't work this way..

#problem 2
# if you use decorators with a function that returns something
# decorators won't work this time also


# fixing the problem 1
def decorator(any_function):
    def wrapper(*args, **kwargs):
        print("I'm enhancing your function")
        any_function(*args, **kwargs)
    return wrapper

@decorator
def func(a):
    print(f"I'm a funtion with an arguement {a}")
func(7)


#fixing problem 2
def decorator2(any_function):
    def wrapper(*args, **kwargs):
        print("I'm enhancing your function")
        return any_function(*args, **kwargs)
    return wrapper

@decorator2
def func2(a,b):
    return a + b
print(func2(2,2))

# if you dont write return in wrapper it means the wrapper is returng nothing
