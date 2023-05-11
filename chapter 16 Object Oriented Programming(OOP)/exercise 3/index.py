class Person:
    person_instance = 0
    def __init__(self, first_name, last_name, age):
        self.f_name = first_name
        self.l_name = last_name
        self.age = age
        Person.person_instance += 1

p1 = Person("Izuku", "Midoriya", 16)
print(Person.person_instance)
p2 = Person("Ochako", "Uraraka", 15)
print(Person.person_instance)
