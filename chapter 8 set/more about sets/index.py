s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

if 2 in s1:
    print("present")
else:
    print("not present")

for item in s2:
    print(item)

union = s1 | s2
print(union)

intersection = s1 & s2
print(intersection)
