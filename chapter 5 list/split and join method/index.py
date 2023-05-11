# we've learn split method in string method. now we will use it with list

# user_info = "deku, 16".split(",")
user_info = "deku 16".split()
print(user_info)

# now user_info is a list and now will print it as a string

print(",".join(user_info))
print(" ".join(user_info))
