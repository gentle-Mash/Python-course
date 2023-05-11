#inheritance is using base class's ability in child class

#this is base class
class Phone:
    def __init__(self, Brand, Model, Price):
        self.brand = Brand
        self.model = Model
        self._price = Price

    def full_name(self):
        return f"you choice is {self.brand} {self.model}"
    
    def make_a_call(self, number):
        return f"calling {int(number)}"
    
#this is child or derived class
#there are two ways of making child class
#way-1---- uncommon way
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

#way---2--- common way

class Telephone(Phone):
    def __init__(self, Brand, Model, Price, RAM, Internal_Memory):
        super().__init__(Brand, Model, Price)
        self.ram = RAM
        self.internal_memory = Internal_Memory

t1 = Telephone("abc", "fg34", 12000, "2GB", "3GB")
print(t1.full_name())
        



