# OOP is so useful with real world programming. you can create your own class like list , tiple etc

# list, tuple, set, dictionary etc are class
# every list, tuple , set , dictionary we made are object
# and the things that enhance our object's functionability are methods like append, pop, delete etc

# some keywords to remember
# init method or constructor
# object or instance 

# step-1--- use class key word and give your class name starting with capital letter(it's a convention you can also write in small letter)
# step--2 --- define init  method or constructor function
# step---3 --- write special word self(it's a convention) in parenthis
# step---4 --- after self write your attributes of your object 
# step---5 --- in inite function declare your instance variables


class Person:
    def __init__(self, first_name, last_name, age):
        # print("person is called")
        self.f_name = first_name
        self.l_name = last_name
        self.your_age = age


p1 = Person("Izuku", "Midoriya", 16)
p2 = Person("Ochako", "Uraraka", 15)
# print(p1)
print(p1.f_name)
print(p2.f_name)