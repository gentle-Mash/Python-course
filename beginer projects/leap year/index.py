print("Leap year finder!!!")

finding_year = int(input("Enter your desire year: ").strip())

if (finding_year % 4 == 0) and (finding_year % 100 != 0) :
    print("It's a Leap year")
elif finding_year % 100 == 0:
    if finding_year % 400 == 0:
        print("It's a Leap year")
else:
    print("It's not a Leap year")
