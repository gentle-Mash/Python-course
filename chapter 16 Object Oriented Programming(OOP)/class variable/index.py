# umm when you have to pass same data in your class method you can use class variable


class Circle:
    pi = 3.1416 # this is class variable
    def __init__(self,radius):
        self.radius =  radius
    def area(self):
        return (4*Circle.pi*(self.radius)**2)
    
c1 = Circle(4)
print(c1.radius)
print(c1.area())
