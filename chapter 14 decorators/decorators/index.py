#decorators enhance your function's functionability
def decorator(any_function):
    def wrapper():
        print("I'm enhancing your function")
        any_function()
    return wrapper


def func1():
    print("it's a function 1")
enhanced = decorator(func1)
enhanced()

# you can also call decorators by using @ like this--- it's called syntactic sugar
@decorator
def func2():
    print("it's a function 2")

func2()