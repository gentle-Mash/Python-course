

class Laptop:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.name = model_name
        self._price =  max(price,0) # this way user can't input negative value
        self.laptop_name = brand+" "+model_name
        self.complete = brand + " " + str(price)
    
    @property
    def specification(self):
        return (f"complete specification {self.brand} {self.name} price:{self.price}")
    
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, new_price):
        self._price = max(new_price,0)

laptop1 = Laptop("hp", "hg432", 62000)
print(laptop1._price)

print(laptop1.complete) # here even you change the price it's not chaning
print(laptop1.specification) # that's why you can use property


laptop1.price = -500000
print(laptop1._price)

