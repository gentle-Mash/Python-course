class Laptop:
    discount_percent = 10
    def __init__(self, Brand, model_name, price):
        self.brand = Brand
        self.model = model_name
        self.price = price
    def discount(self):
        return self.price - ((self.price*self.discount_percent)/100)

laptop1 = Laptop("Macbook", "akjgd73", 980000)
print(laptop1.__dict__)
print(laptop1.discount())


laptop2 = Laptop("hp","jsfhg84ug",600000)
laptop2.discount_percent = 50
print(laptop2.__dict__)
print(laptop2.discount())