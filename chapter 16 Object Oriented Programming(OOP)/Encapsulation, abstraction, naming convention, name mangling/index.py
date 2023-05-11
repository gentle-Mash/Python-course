class Laptop:
    instance_counts = 0                            #
    def __init__(self, brand, model_name, price):  #
        Laptop.instance_counts += 1                #
        self.brand = brand                         # 
        self.name = model_name                     #  
        self.__price =  price                        #  this portion is called Encapsulation
        self.laptop_name = brand+" "+model_name    #
                                                   #
    def full_name(self):                           #
        return print(f"{self.laptop_name}")        #   

laptop1 = Laptop("hp", "hg432", 62000) # this portion is abstraction
laptop1.full_name()                    #
print(laptop1.__dict__)                #
print(laptop1._Laptop__price)          #


# Naming convention 
# _name : when you declare your instance variable like this it means other developer to not change anything from this variable
# __name : it's also called dunder or magic method. when you declare your vaiable like this python change your variable name to _class__name
# and this is name mangling because python change your name
