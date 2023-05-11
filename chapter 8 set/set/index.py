# set is unoredered collection of unique data

s = {1,2,2,3,4,5,6,7,7,7,7,8,9}
print(s)
# so set doesn't store any data twice
l = [1,2,2,3,4,5,6,7,7,7,7,8,8,9]
print(l)
s2 = list(set(l))
print(s2)

s.add(0)
print(s)

s.remove(6)
print(s)

s.discard(11) # when you are removing an item that doesn't exist in set use discard otherwise there will be error
print(s)

s3 =  s.copy()
print(s3)

s.clear()
print(s)

# and you cannot store list, tuple or dictionary in a set :)
