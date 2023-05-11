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
    
    @classmethod
    def from_string(cls, string):
        brand, model_name, price = string.split(",")
        return cls(brand, model_name, int(price))

laptop1 = Laptop("hp", "hg432", 62000)
laptop2 = Laptop("macbook", "gt5g432", 8592000)
print(laptop1.brand)
# print(laptop1.laptop_name)
laptop3 = Laptop.from_string("tohshiba,hty55ht,45000")
print(laptop3.brand)
# Laptop.instance_count()
print((laptop3.price) + 1)
