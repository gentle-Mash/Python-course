# use of parametre in order

# 1 normal parametre-- P
# *args-- A 
# deafault parametre-- D 
# **kwargs-- K

def func(name, *args, age = "unkown", **kwargs):
    print(name)
    print(args)
    print(age)
    print(kwargs)
func("deku",1,2,3,5, a="b", b="c", c="d")

# whatever parametre you use always maintan PADK order means PA, AD, DK, AK, PK, PD 