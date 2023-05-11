

from csv import DictWriter

with open("csvfile.csv","w", newline="") as new:
    csv_writer = DictWriter(new, fieldnames=["name","quirk","age"])
    csv_writer.writeheader()
    csv_writer.writerow({
        "name":"deku",
        "quirk":"OFA",
        "age":16
    })
    csv_writer.writerow({
        "name":"ochako",
        "quirk":"zerp-gravity",
        "age":16
    })

with open("csvfile2.csv","w", newline="") as new2:
    csv_writer = DictWriter(new2, fieldnames=["name","quirk","age"])
    csv_writer.writeheader()
    csv_writer.writerows([{"name":"deku","quirk":"OFA", "age":16},
                          {"name":"ochako","quirk":"zero-gravity", "age":16}
                          ])