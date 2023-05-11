with open("emoji.txt", "r", encoding="UTF-8") as emoji:
    print(emoji.encoding)
    text = emoji.read()
    print(text)


with open("so many words.txt", "r") as rf:
    data = rf.read(100)
    while len(data) > 0:
        print(data)
        data = rf.read(100)