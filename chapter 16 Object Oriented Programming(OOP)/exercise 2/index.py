class Laptop:
    def __init__(self, Brand, model_name, price):
        self.brand = Brand
        self.model = model_name
        self.price = price
    def discount(self,num):
        return self.price - ((self.price*num)/100)

laptop1 = Laptop("Macbook", "akjgd73", 980000)
print(laptop1.discount(17))