from csv import reader, writer

with open("file1.csv","r") as readfile:
    with open("file2.csv","w",newline="") as writefile:
        cvs_reader = reader(readfile)
        cvs_writer = writer(writefile)
        for row in cvs_reader:
            cvs_writer.writerows([row])