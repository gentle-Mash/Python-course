def add(a,b):
    if (type(a) is int) and (type(b) is int):
        return a + b
    raise TypeError("Wrong data type")

print(add(2,3))
print(add(2,"3"))