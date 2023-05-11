# Most python developers avoid multiple inheritence so it's discouraged to us
# but we should know about it

#here I'm quickly making some class without any init function. just writing 2 methods in them just for a short basic example of muoltiple inheritance

class A:

    def class_A_method(self):
        return print("I'm from class A")
    def hello(self):
        return print("Hi class A")
    
class B:

    def class_B_method(self):
        return print("I'm from class B")
    def hello(self):
        return print("Hi class B")
    
class C(A,B): #this is multiple inheritance
    pass # pass means I don't want to write anything in this class

obj_a = A()
obj_b = B()
obj_c = C()

obj_a.class_A_method()
obj_b.class_B_method()

obj_c.hello() # here C has inherited class A first so C is calling the method from class A

# you can check the MRO of class C by help function but there is another way

print(C.mro()) # it will give you a list
# or
print(C.__mro__) # it will give you a tuple