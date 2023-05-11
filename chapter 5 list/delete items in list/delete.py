fruits = ["mango", "jackfruit", "orange", "strwberry", "apple", "orange", "mandarine"]
fruits.pop() #if you don't pass argument by default it will remove the last value
print(fruits)

fruits.pop(1)
print(fruits)

del fruits[2]
print(fruits)

fruits.remove("orange")
print(fruits)