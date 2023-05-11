# dictionaries are like objects in javascript
# create dictionaries way -1
dictionary = {
    "name" : "deku",
    "age"  : 16,
    "quirk": "OFA"
}

print(dictionary)

#way -2 

dictionary2 = dict(name = "Dynamight",
age = 16, quirk = "explosion")

print(dictionary2)

#access data from dictionary. dictionary has no indexing so you can't use index method

print(dictionary["name"])
print(dictionary2["age"])

dictionary3 = {
    "quirk" : "OFA",
    "power" : ["gear shift", "fa-jin", "danger sense"]

}
print(dictionary3)

# add data

dictionary3["another3"] = ["black-whip", "smokescreen", "float"]

print(dictionary3)

dictionary4 = {
    "hero1" : {
        "quirk" : "OFA",
        "power" : ["gear shift", "fa-jin", "danger sense"]
    },
}

print(dictionary4)