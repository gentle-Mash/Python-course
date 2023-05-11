# comprehension
odd_even = {i:("even" if i%2 == 0 else "odd") for i in range(1,11)}
print(odd_even)

# normally
odd_even2 = {}
for i in range(1,11):
    if i%2 == 0:
        odd_even2[i] = "even"
    else:
        odd_even2[i] = "odd"
print(odd_even2)