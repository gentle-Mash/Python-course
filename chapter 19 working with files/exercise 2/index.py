with open("index.html", "r") as rf:
    with open("output.txt","a") as wf:
        for line in rf.readlines():
            if "<a href=" in line:
                first_quote = line.find("\"", line.find("<a href="))
                second_quote = line.find("\"", first_quote+1)
                url = line[first_quote+1 : second_quote]
                wf.write(url + "\n")