# lambda expression is a function which has no name
# that's why it's also called annonymous funtion

# normal function 

def add(a,b):
    return a+b
print(add(2,3))

# lambda expression

add2 = lambda a,b : a+b
print(add2(2,3))

multiply = lambda a,b : a*b
print(multiply(2,3))

# lambda isn't used to store itself in a variable. we are doing it for understanding lambda
# lambda is used with built in funsions like- map, reduce , filter
