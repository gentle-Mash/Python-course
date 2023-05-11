user_info = {}

name = input("what's your name? ").strip()
age = int(input("what's your age? ").strip())
movies = input("what're your favorite movies? please seperate them by comma ").strip().split(",")
songs = input("what're favorite songs?please seperate them by comma ").strip().split(",")

user_info["name"] = name
user_info['age'] = age
user_info['fav_movies'] = movies
user_info['fav_songs'] = songs

# print(user_info)

items = user_info.items()

for i,j in items:
    print(f"{i} : {j}")