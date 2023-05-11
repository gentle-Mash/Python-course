name, character = input("please enter your name and the character you want to count \' please seperate them with comma \'").split(",");
print(f"the length of your name is {len(name)}");
print(f"the number of {character} is {name.lower().count(character.lower())}");