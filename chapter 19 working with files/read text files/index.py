# to open your txt file use open function and write the path in that

my_text = open("deku.txt","r") # you could don't give "r" because by default it's set "r"
# "r" is for read files and "w" is for writing

# to read file use read method
print(my_text.read())

#to sea where your cursor's position use tell method
print(my_text.tell())
#once your coursor is at the last position of your txt file . you can't print your txt file again
# in order to print again you have to set your cursor at first positon

#with seek method you can do this
my_text.seek(0)
print(my_text.tell())
print(my_text.read())
my_text.seek(0)

# if you want to print your text line by line use readline method
print(my_text.readline(), end="")
print(my_text.readline())
my_text.seek(0)


# if you want to store your text in a list use readlines method. and you can do every list things with this list
print(my_text.readlines())
my_text.seek(0)

# if you want to print your txt file name use name attribute
print(my_text.name)


# if you want to know if your file is closed or not use cloased attribute
print(my_text.closed)


# now here my_text is an iterator 
print(my_text)
# so you can also iterate this
for line in my_text:
    print(line, end="")

# for line in my_text.readlines()[:2]:
#     print(line, end="")


# For good codeing behaviour you should always close your file after working with it by close method
my_text.close()


print(my_text.closed)