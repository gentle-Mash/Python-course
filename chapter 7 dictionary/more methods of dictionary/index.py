#if you want to make a dictionary that has several keys with same values 
# you can simply use fromkeys method

d = dict.fromkeys(["name", "age", "quirk"], "unknown")
print(d)

#you can also write like these several ways

e = dict.fromkeys(("name", "age", "quirk"), "unknown")
print(e)

f = dict.fromkeys(["name", "age", "quirk"], ["unknown","known"])
print(f)

g = dict.fromkeys(range(1,11), "unknown")
print(g)

# get method
# if you want to print a key value pair from your dictionary
# which doesn't exist in your dictionary,
# if you simply use print(dictionary["key"]),
#their will be error . so we don't want error 
#to avoid this we should always use get method to access data from dictionary

print(d.get("name"))
print(d.get("names"))

#clear method
# if you want to clear your dictionary you can use this

print(e)
e.clear()
print(e)

#copy method 
#if you want to make another different dictionary with the same values from your other dictionary 
# you can use copy method
# don't use dictionary1 = dictionary2
# it won't seperate the dictionaries. if change something from one of them both will change
# but copy method won't allow it


h = d.copy()
print(h)
print(d)

if h is d:
    print(True)
else:
    print(False)
