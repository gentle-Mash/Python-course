num1 = int(input("enter 1st number ").strip())
num2 = int(input("enter 2nd number ").strip())

def big_numb(num1, num2):
    if num1 > num2:
        return f"{num1} is bigger"
    return f"{num2} is bigger"
print(big_numb(num1,num2))