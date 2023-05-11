import os, shutil
# D:\Gentle Hero\python_course\chapter 22 project 1
file_types = {
    'audio_files' : (".mp3",".wav",".adx"),
    'video_files' : (".mp4",".mkv",".mpeg"),
    'document_files' : (".txt",".pdf"),
}

folder_path = input("enter your folder path: ")
items = os.listdir(folder_path)
def finder_files(extensions):
    files = []
    for file in items:
        for extension in extensions:
            if file.endswith(extension):
                files.append(file)
    return files
    #you could also create the lsit like this
    # return [file for file in os.lisdir(folder_path) for extention in extensions if file.endswith(extension) ]
# print(finder_files(folder_path, document_files))

for file_type, extension_tuple in file_types.items():
    files = finder_files(extension_tuple)
    if files:
        folder_name = file_type.split("_")[0] + " files"
        folderpath = os.path.join(folder_path, folder_name)
        os.mkdir(folderpath)
        for item in files:
            item_path = os.path.join(folder_path, item)
            item_new_path = os.path.join(folderpath,item)
            shutil.move(item_path,item_new_path)
    # print(finder_files(folder_path, extension_tuple))

# here is a new problem thst is it's also creating empty folders for the files that don't exists there




