# instance methods are the functions that are defined in class like append, pop, delete etc

class Person:
    def __init__(self, f_name, l_name, age):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age

    def full_name(self):
        return self.f_name+" "+self.l_name
    def above_18(self):
        return self.age > 18
    
p1 = Person("Izuku", "Midoriya", 16)
print(p1.full_name())
# in background the code turns like this
# print(Person.full_name(p1))
print(p1.above_18())
