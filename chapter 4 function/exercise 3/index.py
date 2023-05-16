

def is_prime_number(num):
    values = []
    for i in range(1, num+1):
        if num % i == 0:
            values.append(True)
        else:
            values.append(False)
    if num == 1:
        print(False)
    elif values.count(True) > 2:
        print(False)
    elif values.count(True) == 2:
        print(True)
    


user_input = int(input("Enter a number: ").strip())

is_prime_number(num=user_input)
# print(2%2 == 0)