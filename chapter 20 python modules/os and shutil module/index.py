import os, shutil

# if you want print complete data of a folder

folder_iter = os.walk(r"D:\Gentle Hero\python_course\chapter 20 python modules\os and shutil module")
print(folder_iter) # it's an iterator and it will give you 3 things

for current_path, folder_names, file_names in folder_iter:
    print(f"current path is {current_path}")
    print(f"folder names {folder_names}")
    print(f"file names {file_names}")

# if you want to make folder in another folder do this

# os.makedirs("new/another")

# os.rmdir("folder 1") # this will delete the empty folders only

# shutil.rmtree("new") #this will delete a folder which can be empty or not parmanently. it won't move the folder to recycle bean

# shutil.copytree("songs","movies/songs2") # this is for copying any folder and u can also rename that copied folder

# shutil.copy("text message.txt", "movies/no text.txt") # this is for copying files

shutil.move("songs","movies/another songs") # this is for moving folder or files



