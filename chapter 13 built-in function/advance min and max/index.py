names = ["izuku", "bakugo", "ochako"]
print(max(names, key = lambda item: len(item)))
print(min(names, key = lambda item: len(item)))

students = [
    {"name":"deku", "rank":1},
    {"name":"shoto", "rank":3},
    {"name":"bakugo", "rank":2}
]

print(min(students, key = lambda item:item.get('rank'))["name"])

students2 = {
    "deku" : {"quirk": "OFA", "rank":1},
    "uravity" : {"quirk": "Zero gravity", "rank":6},
    "sukuyomi" : {"quirk": "Dark Shadow", "rank":4},
}

print(max(students2, key = lambda item:students2[item].get("rank")))