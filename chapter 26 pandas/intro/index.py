import pandas

data = pandas.read_csv("weather.csv")
# print(data) # this is data frame
print(type(data))

# print(data["Temperature (Celsius)"]) # every column in a data frame is called a series
print(type(data["Temperature (Celsius)"]))

# in pandas documentation there is many methods about data frame and series here is an xmpl
# with to_dict() method you can convert your csv data into a dictionary and deal it like a dictionary

data_dict = data.to_dict()  
print(data_dict) 

# like data frame , there is similar kinds of methods for series also liek
# to_list method

series_list = data["Temperature (Celsius)"].to_list()
print(series_list)

print(round(data["Temperature (Celsius)"].mean(), 3)) # this will give me the average of temperatures in my csv file

print(data["Temperature (Celsius)"].max())
print(type(data["Temperature (Celsius)"].max()))

# you can also call your series like this
print(data.Day)


# if you want to print any of your row
print(data[data.Day == "Monday"])

print(data[data["Temperature (Celsius)"] == data["Temperature (Celsius)"].max()])

monday = data[data.Day == "Monday"]
print(monday["Temperature (Celsius)"])

# make data frame from scratch

Heros = {
    "powers" : ["OFA","Zero-gravity","Explosion"],
    "owners" : ["Deku","Uravity","Dynamight"]
}

Hero_data = pandas.DataFrame(Heros)
print(Hero_data)

Hero_data.to_csv("my_hero.csv")