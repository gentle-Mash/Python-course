x = 5
def scope():
    global x
    x = 7
    return x
print(x)
print(scope())