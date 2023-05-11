# tuple is like list but unlike list you can't add or delete or change any elements of tuple
# and offcourse you can store any type of data in tuple
# you can loop tuple as the same as the list
# and you can use common methods like indexing, slicing, count etc and funtion like min, max, len, sum etc
# basically the methods that don't change the tuple's elements


tuple1 = (1,2,4,5,None,True,False,"avb") #it's a tuple
tuple2 = (1,) #it's also tuple tuple with sigle element and don't forget to add comma otherwise it won't be a tuple anymore
tuple3 = "deku", "ochako", 1,2 #it's also a tuple without parenthis

print(type(tuple3))

# unpacking tuple

no1,no5,int_value,int_value2 = (tuple3)

print(no1)
print(no5)
print(int_value)
print(int_value2)

# if you store list inside tuple then you can do list things on that list but not on tuple

tuple4 = (1,2,3,[4,5,6])
tuple4[3].pop()
print(tuple4)
