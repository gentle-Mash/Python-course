import pdb

pdb.set_trace() # you can use this function in anywhere of your code. 
# use your common sesnse where can be the error could happen then set this func 1 or 2 line before

name = input("enter your name ")
age = input("enter your age ")
print(f"your name is {name} and age is {age}")

age_5 = int(age) + 5
print(f"{name} you will be {age_5} after 5 years")

# l -- to see where the code is stuck
# n -- execute the stucked line
# q -- quit the code
# c -- get out from debugging