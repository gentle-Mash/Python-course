izuku = {
    "Hero name" : "deku",
    "age" : 16,
    "quirk" : "OFA"
}

# pop method-- unlike list here you have to pass at least one argument
# and like list it also return the popped item
# it returns just the value with it's original data type
popped_items = izuku.pop("quirk")
print(popped_items)
print(type(popped_items))
print(izuku)

# popitem method -- it randomly delete any item from your dictionary and return the item
# it returns both key and value always as tuple
popped_items2 = izuku.popitem()
print(izuku)
print(popped_items2)
print(type(popped_items2))

