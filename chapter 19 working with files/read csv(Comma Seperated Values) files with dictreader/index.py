from csv import DictReader

with open("file.csv", "r") as new:
    csv_reader = DictReader(new, delimiter="|")
    print(csv_reader)
    #it's also an iterator but it will give u a ordered dictionary
    for row in csv_reader:
        print(row["email"])