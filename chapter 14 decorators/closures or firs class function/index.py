# closures or first class functions are the functions who also return function

def to_power(n):
    def clac_power(x):
        return x**n
    return clac_power

cube = to_power(3)
print(cube(2))