from functools import wraps

def only_data_type(data_type):
    def decorator(function):
        @wraps(function)
        def warapper(*args):
            if all([(type(arg) == data_type) for arg in args]):
                return function(*args)
            return("Invalid data type")
        return warapper
    return decorator

@only_data_type(int)
def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add_all(1,2,3,4))

@only_data_type(str)
def string_add(*args):
    string = ''
    for i in args:
        string += i
    return string

print(string_add("Izuku ", "Midoriya", 1))