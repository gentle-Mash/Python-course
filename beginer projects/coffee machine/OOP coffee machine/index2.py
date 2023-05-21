import os, time, functions
from datas import resources
from datas import MENU


def coffee_maker(coffee_name): # permission to make coffee function
    if functions.is_sufficient(resources, MENU, coffee_name) == True:
        print("Please pay first.")
        functions.making_coffee(resources, MENU, coffee_name)
        time.sleep(5)
        os.system('clear')
        working()
    elif functions.is_sufficient(resources, MENU, coffee_name) == False:
        print(f"Sorry. Shortage of ingredients for your coffee {coffee_name}.")

def working():
    while True:
        print("Welcome to my coffee shop. what you would like to try? here are 3 flavours of Hot Coffee. 'Espresso- $ 1.5 (1)' or 'Latte- $ 2.5 (2)' or 'Cappuccino- $ 3 (3)' ")
        user_choice = input("what's your choice?: ").strip()
        if user_choice == "report":
            for key in resources:
                if key == "coffee":
                    print(f"{key} : {resources[key]} gm")
                elif key == "money":
                    print(f"{key} : $ {resources[key]}")
                else:
                    print(f"{key} : {resources[key]} mL")
            continue
        elif user_choice == "1":
            coffee_maker("espresso")
            break
        elif user_choice == "2":
            coffee_maker("latte")
            break
        elif user_choice == "3":
            coffee_maker("cappuccino")
            break
        elif user_choice == "off":
            print("Shutting down")
            break        
        else:
            print("Type 1 or 2 or 3")

working()
