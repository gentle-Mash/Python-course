squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)

squares2 = [i**2 for i in range(1,11)]
print(squares2)

names = ["Deku", "Ochako", "Lida"]
names2 = []
for name in names:
    names2.append(name[0])
print(names2)

names3 = [name[0] for name in names]
print(names3)