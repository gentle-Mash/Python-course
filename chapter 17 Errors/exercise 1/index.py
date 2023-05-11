try:
    a = int(input("enter the number you want to divide "))
    b = int(input("enter the number you want to divide by "))
except ValueError as err:
     print(err)

def divide(n1,n2):
        try:
            return (n1/n2)
        except ZeroDivisionError as err:
            print("Math error. No number can be divided by 0")
        except ValueError as err:
            print(err)
        except:
             print("unexpected error")
        finally:
            print("thanks for using our service. your ans is ")
try:
    print(divide(a,b))
except NameError:
     pass