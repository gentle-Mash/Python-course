# static method has nothing to do with your class or object
# it's a logical function that is made in class when we need it
# it's made with static method decorator

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
    
    @staticmethod
    def hello(): #you don't need to pass any arguement here as it's not related to our class or object
        return print("I'm from static method")

laptop1 = Laptop("hp", "hg432", 62000)
laptop2 = Laptop("macbook", "gt5g432", 8592000)
laptop3 = Laptop.from_string("tohshiba,hty55ht,45000")

Laptop.hello()
