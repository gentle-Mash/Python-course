from functools import wraps

def print_function_data(any_function):
    @wraps(any_function)
    def wrapper(*args, **kwargs):
        print(f"you are calling {addition.__name__} function")
        print(addition.__doc__)
        return any_function(*args, **kwargs)
    return wrapper

@print_function_data
def addition(a,b):
    '''this function takes 2 values and returns their sum'''
    return a+b
print(addition(5,4))