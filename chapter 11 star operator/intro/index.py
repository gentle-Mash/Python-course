def summ(a,b):
    return a+b
print(summ(4,6))

# in this function we cannot pass more than 2 arguements
# if we want that we have to use * star operator

def star(*args):
    print(args)
star(1,2,3,45,6,7,8)

# by doing this we can pass as mane arguements as we want 
# and it will give us a tuple made of all that arguements

def summ2(*args):
    total = 0
    for i in args:
        total += i
    return total
print(summ2(1,2,3,4))

#here we are passing that tuple in thyat for loop
#and as a convention always use args after *