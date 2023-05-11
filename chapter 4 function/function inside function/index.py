num1 = int(input("enter number 1 "))
num2 = int(input("enter number 2 "))
num3 = int(input("enter number 3 "))

def bigger(num1, num2):
    if num1>num2 :
        return num1
    return num2


def biggest(num1, num2, num3):
    big = bigger(num1, num2)
    return bigger(big, num3)
print(biggest(num1, num2, num3))

# you could also code like this

# def biggest(num1, num2, num3):   
#     return bigger(bigger(num1, num2), num3)
# print(biggest(num1, num2, num3))