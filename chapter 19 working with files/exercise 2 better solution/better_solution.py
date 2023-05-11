# the previous code doesn't work for multiple links in one line
# but this one does


with open("index.html", "r") as rf:
    with open("output2.txt","a") as wf:
        page = rf.read()
        found_char = True
        while found_char:
            pos = page.find("<a href=")
            if pos == -1:
                found_char = False
            else:
                first_quote = page.find("\"", page.find("<a href="))
                second_quote = page.find("\"", first_quote+1)
                url = page[first_quote+1 : second_quote]
                wf.write(url + "\n")
                page = page[second_quote:]
                
                