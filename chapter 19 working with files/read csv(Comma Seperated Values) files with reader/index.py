# in csv files u can also use *, | but comma is convention
# to read csv we have to use reader or dictreader function from csv module

from csv import reader


with open("file.csv", "r") as new:
    csv_reader = reader(new) # it's an iterator so you can use every iterator thing
    print(csv_reader)
    next(csv_reader) # to avoid the header of your csv file
    for row in csv_reader:
        print(row)