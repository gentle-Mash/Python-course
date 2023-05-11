import time
from functools import wraps

def calculate_time(any_function):
    @wraps(any_function)
    def wrapper():
        t1 = time.time()
        any_function()
        t2 = time.time()
        print(f"this function took {t2-t1} seconds to run")
    return wrapper

@calculate_time
def func():
    print("this is function")
func()

def calc_time(any_function):
    @wraps(any_function)
    def wrapper(*args, **kwargs):
        print(f"you are executing {any_function.__name__} function")
        t1 = time.time()
        returned = any_function(*args, **kwargs)
        t2 = time.time()
        print(f"it took {t2-t1} seconds to run")
        return returned
    return wrapper

@calc_time
def list_of_squres(n):
    return [i**2 for i in range(1, n+1)]
list_of_squres(30000)

