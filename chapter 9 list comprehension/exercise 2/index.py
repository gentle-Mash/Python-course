list1 = [True, False, 1,2,3.0,4.5,[1,2,3], None, "deku"]
numbers = []
for i in list1:
    if type(i) == int or type(i) == float:
        numbers.append(str(i))
print(numbers)

def num_to_str(l):
    return [str(i) for i in l if type(i) == int or type(i) == float]
print(num_to_str(list1))