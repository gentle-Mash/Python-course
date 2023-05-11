# here smartphone is inheriting phone again iphone is inheriting smarphone.. this is called multilevel inheritance

class Phone:
    def __init__(self, Brand, Model, Price):
        self.brand = Brand
        self.model = Model
        self._price = Price

    def full_name(self):
        return f"you choice is {self.brand} {self.model}"
    
    def make_a_call(self, number):
        return f"calling {int(number)}"

class Smartphone(Phone):
    def __init__(self, Brand, Model, Price, RAM, Internal_Memory, Front_Camera, Back_Camera):
        Phone.__init__(self,Brand, Model, Price)
        self.ram = RAM
        self.internal_memory = Internal_Memory
        self.front_camera = Front_Camera
        self.back_camera = Back_Camera

p1 = Phone("Nokia", "1200", 990)
s1 = Smartphone("Techno", "kdsjg44", 15000, "8GB", "64GB", "6MP", "16MP")

print(p1.full_name())
print(s1.full_name())


class Iphone(Smartphone):
    def __init__(self, Brand, Model, Price, RAM, Internal_Memory, Front_Camera, Back_Camera, Display):
        super().__init__(Brand, Model, Price, RAM, Internal_Memory, Front_Camera, Back_Camera)
        self.display = Display

i1 = Iphone("abc", "fg34", 12000, "2GB", "3GB", "12MP", "24MP","6.5 inch")
print(i1.full_name())
        
# MRO --- Method Resulation Order
# for phone class python will search only in Phone
# for smartphone class python will search at first in Smartphone if he fails to find he will search in Phone
# for iphone class python will search at first in iphone if he fails to find he will search in Smarthone and if fails agein he will search in Phone
 
# Suppose python found a function in your child class he won't go to your parent class even though the same named function is also in your parent calss
# this is called method overriding

# 2 built in function about class
# 1 isinstance()
# 2 issubclass()

print(isinstance(i1, Iphone))
print(isinstance(i1, Smartphone))
print(isinstance(i1, Phone))
print(isinstance(s1, Iphone))


# is Iphone is a subclass of samrtphone
print(issubclass(Iphone, Smartphone))
print(issubclass(Smartphone, Iphone))

print(help(Smartphone))