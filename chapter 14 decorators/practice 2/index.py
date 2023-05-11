# we are making a decorator that forced user to input a single data type data
from functools import wraps

def only_int_allow(any_function):
    @wraps(any_function)
    def wrapper(*args):
        if all([(type(arg) == int or type(arg) == float) for arg in args]):
            return any_function(*args)
        return ("invalid data type")
    return wrapper
        
@only_int_allow
def add_all(*args):
    total = 0 
    for i in args:
        total += i
    return total

print(add_all(1,2,3,4,5.6))