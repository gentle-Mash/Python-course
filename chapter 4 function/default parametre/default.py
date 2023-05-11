def user_info(fname, lname, age=None):
    print(f"your first name is {fname}")
    print(f"your last name is {lname}")
    print(f"you\'r {age} years old")

user_info("izuku", "midoriya", )

# this isn't right

# def user_info(fname="unknown", lname, age=None):
#     print(f"your first name is {fname}")
#     print(f"your last name is {lname}")
#     print(f"you\'r {age} years old")

# user_info("izuku", "midoriya", )
# you have to define the default parametres from right to left always