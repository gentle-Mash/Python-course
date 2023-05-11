# "w"   mode

with open("deku.txt", "w") as wr:
    wr.write("he is the number 1 hero\nand he will marry uraraka") 
    # "w" will over write your text. means it will delete all your previous text and then it will write

with open("ochako.txt", "w")as o: #though you didn't create your txt file w mode will automatically create this file and write
    o.write("I kind of like deku")


# "a" mode --> if you don't want to delete your previous text then you can use a mode
# and it can also create new files like w mode


with open("deku.txt", "a") as deku:
    deku.write("\nhe is the 9th weilder of OFA")


# "r+" mode --> this is for both read and write
# and it cannot create new files


with open("index.txt", "r+") as rw:
    # rw.write("that's great man") # it will replace previous text with this only by the new text character number. and nothing else will remove
    # but if you want write after the previous text do this
    rw.seek(len(rw.read()))
    rw.write("now it's ok")