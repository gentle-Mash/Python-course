def avereage_finder(*args):
    average = []
    for pairs in zip(*args):
        average.append(sum(pairs)/len(pairs))
    return average

# the same function you can write with lambda expressions
avereage = lambda *args:[sum(pairs)/len(pairs) for pairs in zip(*args)]

print(avereage_finder([1,2,3],[4,5,6],[7,8,9]))
print(avereage([1,2,3],[4,5,6],[7,8,9]))

#by the way these functions are doing this
# (1+4+7)/3 , (2+5+8)/3, (3+6+9)/3