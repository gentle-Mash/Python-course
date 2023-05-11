izuku = dict(hero_name = "deku",
             age = 16,
            quirk = "OFA",
             inner_quirks = 7 )
# key method
izuku_keys = izuku.keys()
print(izuku_keys)
print(type(izuku_keys))
#values method
izuku_values = izuku.values()
print(izuku_values)
print(type(izuku_values))

if "hero_name" in izuku: #by default it will check the keys
    print("present")

#if want to find the values you have to do like this
if "deku" in izuku.values():
    print("present")

for i in izuku:
    print(i)

for i in izuku:
    print(izuku[i])

# items method

item = izuku.items()
print(item)
# it's giving me a values that looks like a list made of many tuples
# but it's neither list nor tuple.
print(type(item))

for i in izuku.items():
    print(i)

for i,j in izuku.items():
    print(f"key is {i} and value is {j}")

# though it's not tuple but it's working like tuple unpacking



