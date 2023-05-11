names = ["deku", "dynamight", "shoto"]
ranks = [1,2,3]
quirks = ["OFA", "Explosion", "Half cold half hot"]

print(list(zip(names,ranks)))
#it's giving me zip objects that is made of tuple
# if you remove an item from one of your lists the zip won't count the odd pair

print(dict(zip(names,ranks)))
print(tuple(zip(names,quirks,ranks)))
# you cannot make dictionary like this when you are working with more than 2 iterables

odd_even = [(1,2),(3,4),(5,6),(7,8)]
print(list(zip(*odd_even)))
# by using * operator your zip object will be unpacked
l1,l2 = list(zip(*odd_even))
print(list(l1))
print(list(l2))



new_list = []
for pairs in odd_even:
    new_list.append(max(pairs))

print(new_list)



# new_list2 = []
# for i in range(4):
#     if l1[i] < l2[i]:
#         new_list2.append(l2[i])
# print(new_list2)

