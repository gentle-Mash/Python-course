num1 = int(input("enter 1st number ").strip())
num2 = int(input("enter 2nd number ").strip())
num3 = int(input("enter 3rd number ").strip())

def biggest_numb(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return f"{num1} is the biggest"
    elif num2 > num1 and num2 > num3:
        return f"{num2} is the biggest"
    return f"{num3} is the biggest"
print(biggest_numb(num1,num2,num3))