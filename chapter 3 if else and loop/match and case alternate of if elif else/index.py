x = input("student name: ")


# match x:
#     case "Harry":
#         print("Griffindore")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Data not found")

match x:
    case "Harry" | "Harmionea" | "Ron":
        print("Griffindore")
    case "Draco":
        print("Slytherin")
    case _:
        print("Data not found")

