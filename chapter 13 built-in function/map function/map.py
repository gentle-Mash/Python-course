# it is used when you pass every items of your list, tuple , string through a single sunction
def add2(a):
    return a+2

numbers = [1,2,3,4,5,6,7]

print(map(add2, numbers))
# so it's giving me a map object. I can store it in a variable as a list or tuple

result = list(map(add2, numbers))
print(result)

# and if you don't store it as a list or tuple you can loop this only one time

result2 = map(add2, numbers)
for i in result2:
    print(i)
for i in result2:
    print(i)
 