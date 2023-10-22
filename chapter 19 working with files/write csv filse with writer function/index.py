from csv import writer

with open("file1.csv", "w", newline="") as ben: # here newline is to avoind blank lines in csv files
    mithai = writer(ben)
    # here you can use 2 methods to write your csv files
    # writerow method
    mithai.writerow(["name","country"])
    mithai.writerow(["Deku","Japan"])
    mithai.writerow(["Mina","Bangladesh"])

with open("file2.csv", "w", newline="") as new: # here newline is to avoind blank lines in csv files
    sid = writer(new)
    # writerows method
    sid.writerows([["Bakugo","Japan"]])
    