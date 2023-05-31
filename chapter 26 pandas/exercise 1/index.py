import pandas

squirrels = pandas.read_csv("squirrel data.csv")
furs = squirrels["Primary Fur Color"].to_dict()


gray = [color for color in furs.values() if color == "Gray"]
black = [color for color in furs.values() if color == "Cinnamon"]
cinnamon = [color for color in furs.values() if color == "Black"]

data = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "count" : [len(gray),len(cinnamon),len(black)]
}

csv = pandas.DataFrame(data)
csv.to_csv("squirrel color count.csv")