# there is another way to read text files by with blocks
# in this way don't have to close the file
# by deafault it will be closed

with open("deku.txt","r") as my_text:
    print(my_text.read())
    # and on and on like previous file
    # we should use this way
    