def multiply(*args):
    multi = 1
    for i in args:
        multi *= i
    return multi
print(multiply(1,2,3,4))

def multiply2(num, *args):
    print(num)
    print(args)

print(multiply2(1,2,3,4,5,6))

# so if you add several parametre with args then 1st arguements will pass to 1st parametre
# and others will make tuple

# you always have to add normal parametre at firts then args
#otherwise there will be error
#because if you don't pass any arguement in normal parametre there will be error