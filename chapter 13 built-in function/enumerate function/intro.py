names = ["deku", "ochako", "lida", "shoto", "asui"]

position = 0
for i in names:
    print(f"{position} ----> {i}")
    position += 1

# this same work we can do with enumerate function

for pos, name in enumerate(names):
    print(f"{pos} ----> {name}")

def finding(l, name):
    for pos, nm in enumerate(l):
        if nm == name:
            return print(pos)
    return print(-1)

finding(names, "lida")
 