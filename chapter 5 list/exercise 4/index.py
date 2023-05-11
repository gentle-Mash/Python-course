numbers = [1,2,3,4,5,6,7,8,9]

def filter_odd_even(l):
    odd_numbers = []
    even_nembers = []
    filtred_numbers = []
    for i in l:
        if i%2 == 0:
            even_nembers.append(i)
        else:
            odd_numbers.append(i)
    filtred_numbers.append(odd_numbers)
    filtred_numbers.append(even_nembers)
    return filtred_numbers

print(filter_odd_even(numbers))

