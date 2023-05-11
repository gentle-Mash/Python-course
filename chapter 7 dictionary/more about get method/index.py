# we know that if get didn't find the key, by default it prints None.
# if we want to print different line in these case you can do this

d = dict(name = "deku",  age = 16)
print(d.get("names", "not found !"))

d = {
    "name" : "deku",
    "age" : 16,
    "age" : 18
}
print(d)
# so if your dictionary has same keys the later key will count
# but if you made your dict method there will be error