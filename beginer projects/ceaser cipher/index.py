alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type \'Encrypt\' to encode your text or type \'Decode\' to decode your text:\n").title().strip()

text = input("Enter your text:\n").lower().strip()

shift = int(input("Enter your shift number to decode or encode your text:\n").strip())

def encrypt(text, shift):
    encrypt_text = []
    for i in range(len(text)):
            if text[i] in alphabet:
                index_pos = alphabet.index(text[i])
                encrypt_text.append(alphabet[index_pos+shift])
            else:
                encrypt_text.append(text[i])
    encrypt_msg = ""
    for i in range(len(text)):
        encrypt_msg += encrypt_text[i]
    
    return encrypt_msg

# print(encrypt(text, shift))

def decode(text, shift):
    decode_text = []
    for i in range(len(text)):
            if text[i] in alphabet:
                index_pos = alphabet.index(text[i])
                decode_text.append(alphabet[index_pos - shift])
            else:
                decode_text.append(text[i])
      

    decode_msg = ""
    for i in range(len(text)):
        decode_msg += decode_text[i]
    
    return decode_msg

# print(decode(text, shift))
if direction == "Encrypt":
     print(f"your message is {text}")
     print(f"Encrypted: {encrypt(text, shift)}")
elif direction == "Decode":
     print(f"your message is {text}")
     print(f"Decoded: {decode(text, shift)}")



  
