heroes = ["deku", "dynamight", "shoto"]
print(heroes)
heroes.append("uravity")  #to add value at the end of your list
heroes.append("froppy")  #and you can add just one value each time you use append
print(heroes)

heroes.insert(1, "ingenium") #to add values in any position of your list
print(heroes) #and it also adds just one value each time. here 1 is defining the list position 
               #you want to add values

Heroes = ["red riot", "charge bolt", "sukuyomi"]

list_2 = heroes + Heroes #to concatinate lists
print(Heroes)
print(list_2)

Heroes.extend(heroes) #to add another list's value
print (Heroes)

girls = ["creaty", "acid women", "earphone jack"]
#to add list inside list you can do this by append method

Heroes.append(girls)
print(Heroes)

