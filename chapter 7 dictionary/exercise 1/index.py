def cube(n):
    cubed = {}
    for i in range(1,n+1):
        cubed[i] = i**3
    return cubed
print(cube(10))