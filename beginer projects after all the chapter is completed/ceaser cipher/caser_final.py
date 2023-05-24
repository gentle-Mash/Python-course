alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caeser(direction, text, shift):
    modified_text = ""
    
    if shift >= 26:
        shift = shift % 26

    if direction == "Decode":
        shift *= -1
    for i in text:
        if i in alphabet:
            index = alphabet.index(i)
            new_pos = index + shift
            modified_text += alphabet[new_pos]
        else:
            modified_text += i

    return modified_text

while True:
    direction = input("Type \'Encrypt\' to encode your text or type \'Decode\' to decode your text:\n").title().strip()

    text = input("Enter your text:\n").lower().strip()

    shift = int(input("Enter your shift number to decode or encode your text:\n").strip())

    print(f"caesed msg:\n{caeser(direction, text, shift)}")

    user_info = input("if you want to decode or encode again type \'yes\' otherwise type \'no\'\n").strip()

    if user_info == "yes":
        continue
    else:
        print("Goodbye")
        break











  
