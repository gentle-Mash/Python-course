
user_input = input("enter your string ").strip()

def is_palindrome(user_input):
    if user_input == user_input[::-1]:
        return True
    return False
print(is_palindrome(user_input))

# pythonic code
# def is_palindrome(user_input):
#     return user_input == user_input[::-1]