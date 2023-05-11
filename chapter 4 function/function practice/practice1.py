def last_char(user_name):
    return print(user_name[-1])

last_char("deku")

# def odd_even(x):
#     if x%2 == 0:
#         print(f"{x} is is even")
#     else:
#         print(f"{x} is odd")

# odd_even(5)

def odd_even(x):
    if x%2 == 0:
        return print(f"{x} is is even")
    return print(f"{x} is odd")
odd_even(1)

def is_even(a):
    if a%2 == 0:
        return True
    return False
print(is_even(5))

# pythonic way

def even(j):
    return j%2 == 0
print(even(3))

# funtion without parametre

def deku():
    return "go beyond. plus ultra"
print(deku())