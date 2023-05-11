list1 =[2,4,6,8,10]
list2 = [1,2,3,5,7,9]

print(all([num%2==0 for num in list1]))
print(all([num%2==0 for num in list2]))

print(any([num%2==0 for num in list2]))


def add(*args):
    total = 0
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        for num in args:
            total += num
        return total
    else:
        return "wrong input"

print(add(1,2,3,4,5.5,"deku"))