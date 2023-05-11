import os

print(os.getcwd()) #--> to see my curent working directory
os.chdir(r"D:\Gentle Hero\python_course\chapter 19 working with files") #--> to change my directory
print(os.getcwd())

os.chdir(r"D:\Gentle Hero\python_course\chapter 20 python modules\os module") 

# os.mkdir("movies") #--> to make folders to my current directory

# os.mkdir(r"D:\Gentle Hero\python_course\chapter 21") #--> to make folders to any directory

# I've commented those 2 line because you cannot create a folder which is already exists

print(os.path.exists("movies")) # to see if a folder is already exists or not
if os.path.exists("songs"):
    print("already exists")
else:
    os.mkdir("songs")

open("file.txt", "a").close() #--> easiest way to create a file. and it doesn't care if the file is already exists or not. it wont give error or create any duplicate file

print(os.listdir()) #--> to see my current directory items 
print(os.listdir(r"D:\Gentle Hero\python_course")) #--> to see my any directory items

# those 2 line will give you list of your items o fthat directory 

# there is 2 way you can print your paths. this is the way you shouldn't try

for item in os.listdir():
    print(r"D:\Gentle Hero\python_course\chapter 20 python modules\os module"+"\\"+item)

# this is the way you should try

for item in os.listdir():
    print(os.path.join(os.getcwd(),item))

for item in os.listdir(r"D:\Gentle Hero\python_course\chapter 8 set"):
    print(os.path.join(r"D:\Gentle Hero\python_course\chapter 8 set",item))
