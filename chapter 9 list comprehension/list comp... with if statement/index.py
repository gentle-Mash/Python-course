list1 = list(range(1,11))
even = []
for i in list1:
    if i%2==0:
        even.append(i)
print(even)

even2 = [i for i in list1 if i%2 == 0 ]
print(even2)