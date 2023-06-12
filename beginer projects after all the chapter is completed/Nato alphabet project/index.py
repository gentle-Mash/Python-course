import pandas

data = pandas.read_csv("nato_alphabets.csv")
# print(data)
# data_dict = data.to_dict()
# print(data_dict)

data_dict = {row.letter:row.code for (index,row) in data.iterrows()}
# print(data_dict)
user_input = input("Enter your word\n").upper()

nato_list = [data_dict[word] for word in user_input]
print(nato_list)