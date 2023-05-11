user_name = input("enter your name ").strip()

counted_char = ""
for i in range(len(user_name)):
    if user_name[i] not in counted_char:
        counted_char += user_name[i]
        print(f"{user_name[i]} : {user_name.count(user_name[i])}")