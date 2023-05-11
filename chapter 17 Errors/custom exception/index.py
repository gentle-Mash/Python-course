class NameTooShortError(ValueError):
    pass

username = input("enter your name ")

def validity(name):
    if len(name) < 8:
        raise NameTooShortError("enter a name longer than 8 letters")


validity(username)
print(f"hello {username}")