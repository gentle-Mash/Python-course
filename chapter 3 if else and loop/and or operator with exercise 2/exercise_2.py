name, age = input("enter your name and age ").split();

first_letter = name.lower().strip()[0];
req_letter = "a";

if first_letter == req_letter and int(age) >= 15:
    print("you can watch coco")
else:
    print("you can't watch this movie sorry :)")
