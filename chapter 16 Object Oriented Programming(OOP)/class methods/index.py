# class methods aren't that useful . so u could skip this but you should know about this

class Laptop:
    instance_counts = 0
    def __init__(self, brand, model_name, price):
        Laptop.instance_counts += 1
        self.brand = brand
        self.name = model_name
        self.price =  price
        self.laptop_name = brand+" "+model_name
    @classmethod
    def instance_count(cls): #according to convention we should write cls but you can also write your class name
        return print(f"you have made {cls.instance_counts} instances of {cls.__name__} class ")

laptop1 = Laptop("hp", "hg432", 62000)
laptop2 = Laptop("macbook", "gt5g432", 8592000)
print(laptop1.price)
print(laptop1.laptop_name)
Laptop.instance_count()
# laptop1.instance_count() you could also write like this but this isn't appropiate