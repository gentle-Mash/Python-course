# def decorator(any_function):
#     def wrapper(*args, **kwargs):
#         print("I'm enhancing your function")
#         any_function(*args, **kwargs)
#     return wrapper

# @decorator
# def func(a):
#     print(f"I'm a funtion with an arguement {a}")
# func(7)

# here if you use doc string on func the result will come from wraper func
# let's fix this problem

from functools import wraps

def decorator(any_function):
    @wraps(any_function)
    def wrapper(*args, **kwargs):
        '''this is wrapper function'''
        print("I'm enhancing your function")
        any_function(*args, **kwargs)
    return wrapper

@decorator
def func(a):
    '''this is func function'''
    print(f"I'm a funtion with an arguement {a}")
func(7)

print(func.__name__)
print(func.__doc__)

# now everything is perfect for decorators
