alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type \'Encrypt\' to encode your text or type \'Decode\' to decode your text:\n").title().strip()

text = input("Enter your text:\n").lower().strip()

shift = int(input("Enter your shift number to decode or encode your text:\n").strip())

def caeser(direction, text, shift):
    if direction == "Encrypt":
        encrypt_text = ""
        for i in range(len(text)):
            if text[i] in alphabet:
                index_pos = alphabet.index(text[i])
                encrypt_text += (alphabet[index_pos+shift])
            else:
                encrypt_text += (text[i])
        print(f"your text is: {text}")
        return f"Encrypted: {encrypt_text}"
    
    elif direction == "Decode":
        decode_text = ""
        for i in range(len(text)):
            if text[i] in alphabet:
                index_pos = alphabet.index(text[i])
                decode_text += (alphabet[index_pos - shift])
            else:
                decode_text += (text[i])
        print(f"your text is: {text}")
        return f"Decoded: {decode_text}"


print(caeser(direction, text, shift))








  
