# when you need to define same named function in your every subclass use NotImplemented error

class Animal:
    def __init__(self,name):
        self.name = name
    def sound(self):
        raise NotImplemented("you didn't define any funtion like that in this class")
    
class Birds(Animal):
    def __init__(self,name,species):
        super().__init__(name)
        self.species = species
    # def sound(self):
    #     return "chui chui"
    
b1 = Birds("parrot", "pakhi")
print(b1.sound())
