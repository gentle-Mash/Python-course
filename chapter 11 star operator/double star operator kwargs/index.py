# **kwargs --> key words argument
# unlike *args, it creats a dictionary

def func(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for i,j in kwargs.items():
        print(f"{i} : {j}")
func(f_name = "izuku", l_name = "midoriya")

# dictionary unpacking

d = dict(f_name = "Ochako", l_name = "Uraraka", age = 16)

func(**d)

#like *args you can add several parametre and for that rules are the same