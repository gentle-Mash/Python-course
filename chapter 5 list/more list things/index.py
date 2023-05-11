numbers = list(range(1,11))
print(numbers)

print(numbers.pop())
print(numbers)

print(numbers.index(5))

new_num = [1,3,5,1,5,6,7,1,8]
print(new_num.index(1))
print(new_num.index(1, 1))
print(new_num.index(1, 4))
# print(new_num.index(1, 4, 7))

def negative_list(l):
    neg_list = []
    for i in l:
        neg_list.append(-i)
    return neg_list

print(negative_list(new_num))