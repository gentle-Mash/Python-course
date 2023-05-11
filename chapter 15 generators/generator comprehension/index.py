# generator comprehension is exactly same as list comprehension 
# just you have to use parenthis instead of 3rd brackets

square = (i**2 for i in range(1,11))
print(square)

for i in square:
    print(i)