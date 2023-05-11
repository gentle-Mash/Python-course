

def even_numbers(n):
    for i in range(1,n+1):
        if i%2 == 0:
            yield i
# here after generating our generator we are using loop and we can do this just 1 time

generator = even_numbers(10)
for i in generator:
    print(i)
for i in generator:
    print(i)

# but if we generate our generator in loop we can use this as much as we can
for i in even_numbers(5):
    print(i)
for i in even_numbers(5):
    print(i)

# you could also made even_numbers function like this
# def even_numbers(n):
#     for i in range(2,n+1,2):
#         yield i

