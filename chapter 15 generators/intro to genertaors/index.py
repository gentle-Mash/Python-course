# generators are like list and tuples the difference is list or tuple s are iterables 
# but generators are iterator
# why use generator ?
# beacause it uses less memory than iterables. it doesn't mean that iterables are bad and we shouldn't use them
# when you are working with a sequence of data for once then you should use generators
# other wise iterables are perfect

# you can create generator by making generator function or generator comprehension


def numbers(n):
    for i in range(1,n+1):
        yield(i) # you can also write (yeild i)

generator = numbers(10)
print(generator)

for i in generator:
    print(i)

# you can use this loop just one time beacause generator is a generator :)
# but you can change generator into list or any iterables then you can loop this as much as you want

list1 = list(numbers(10))
for i in list1:
    print(i)