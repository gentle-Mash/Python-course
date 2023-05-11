numbers = list(range(1,6))

def square_numbers(l):
    square = []
    for i in l:
        square.append(i**2)
    return square

print(square_numbers(numbers))