# let's talk about __str__ and __repr__ dunder
# if you want to print your obj like a list which give us a actual list you can use these 2 dunder
class Phone:
    def __init__(self, Brand, Model, Price):
        self.brand = Brand
        self.model = Model
        self._price = Price

    def full_name(self):
        return f"you choice is {self.brand} {self.model}"
    
    def make_a_call(self, number):
        return f"calling {int(number)}"
    
    def __str__(self):
        return f"your chose {self.brand} {self.model}"
    
    def __repr__(self):
        return f"your chose {self.brand} {self.model} price: {self._price}"

p1 = Phone("Nokia","1200",1500)
print(p1) # if you simply print like this by default your str dunder will be called
# so you can specify what you want to print
print(repr(p1)) 
print(p1.__repr__()) # if you write str instead of repr str dunder will be called

# so which one should we use?
# well string formating--- use str
# print the actual object --- use repr

class Smartphone:
    def __init__(self, Brand, Model, Price):
        self.brand = Brand
        self.model = Model
        self._price = Price

    def full_name(self):
        return f"you choice is {self.brand} {self.model}"
    
    def make_a_call(self, number):
        return f"calling {int(number)}"
    
    def __repr__(self):
        return f"Smartphone(\'{self.brand}\' \'{self.model}\' {self._price})"
    
    #len dunder
    def __len__(self):
        return len(self.full_name())
    
    # overload operator 
    def __add__(self, other): # same thing for multiply, substraction, divide etc just change add dunder with their dunder
        return self._price + other._price
    
my_Smartphone = Smartphone("Samsung", "A1", 65000)
my_Smartphone2 = Smartphone("Techno", "bgm231", 15000)
print(my_Smartphone.__repr__())

print(my_Smartphone.__len__()) #len dunder
print(my_Smartphone + my_Smartphone2) # overloading operator

# Polymorphysm
# method overriding, overloading operator, both are polymorphysm
# it means you can concatinate strings , do sum with a single operator (+)
# when you override a method you can apply the same method in different class obj. but the result comes different

