# filter is used when you want some specific items from your list or tuple

def is_even(a):
    return a%2 == 0

numbers = [1,2,3,4,5,6,7,8,9]

result = tuple(filter(is_even, numbers))
print(result)

# you can also define the function inside filter func with lambda expressions
# same goes for map func

result2 = list(filter(lambda a:a%2==0 , numbers))
print(result2)

# and rules are same as map for filter