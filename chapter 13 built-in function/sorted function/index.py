# you can use sort method with list
# but as tuples are immutable you can't use use sort method
#you have to use sorted function
#same goes for sets

tupls = ('banana','grapes','apple')
sorted(tupls)
print(tupls)
# so it won't change our original tuple but it will return us a sorted list of our tuple
print(sorted(tupls))

# advance use 

product_price = [
    {"name":"apple", "price":8500000},
    {"name":"samsung", "price":9500000},
    {"name":"HTC", "price":1500000}
]

print(sorted(product_price, key= lambda item: item.get("price")))
print(sorted(product_price, key= lambda item: item.get("price"), reverse= True))