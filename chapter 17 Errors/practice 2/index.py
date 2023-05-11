class Phone:
    def __init__(self,name):
        self.name = name

class Smartphone:
    def __init__(self):
        self.mobiles = []
    def add(self, new_mobile):
        if isinstance(new_mobile, Phone):
            self.mobiles.append(new_mobile)
        else:
            raise ValueError("the value you input should have been the object of Phone class")

p1 = Phone("Nokia C2")
mobile = Smartphone()
phn = "Iphone"

print(mobile.mobiles)
mobile.add(p1)
print(mobile.mobiles)
print(mobile.mobiles[0].name)

mobile.add(phn)

