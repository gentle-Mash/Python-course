import os, time


#************************************************* Datas **************************************************
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk" : 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
    "money": 0,
}
#************************************************* Datas **************************************************


#************************************************* functions **************************************************
def total_amount(): # money processing function
    
    q = int(input("How many quarters: ").strip()) * 0.25
    d = int(input("How many dimes: ").strip()) * 0.10
    n = int(input("How many nickles: ").strip()) * 0.05
    p = int(input("How many pennis: ").strip()) * 0.01

    total_price = q + d + n + p
    return total_price


def machine_money_count(coffee_name): # keep track of total sell
    resources["money"] += MENU[coffee_name]["cost"]


def is_sufficient(coffee_name): # ingredients checking function
    if (resources["water"] >= MENU[coffee_name]["ingredients"]["water"]) and (resources["milk"] >= MENU[coffee_name]["ingredients"]["milk"]) and (resources["coffee"] >= MENU[coffee_name]["ingredients"]["coffee"]):
        return True
    return False


def making_coffee(coffee_name):  # main coffee maker function 
    user_given_amount = total_amount()
    if user_given_amount < MENU[coffee_name]["cost"]:
        print("Sorry. Not enough money. Money refunded")
    elif user_given_amount > MENU[coffee_name]["cost"]:
        change = user_given_amount - MENU[coffee_name]["cost"]
        print(f"Here is your change ${round(change, 3)} and your {coffee_name}.Enjoy!")
        for key in resources:
            if key != "money":
                resources[key] = resources[key] - MENU[coffee_name]["ingredients"][key]
            else:
                machine_money_count(coffee_name)


def coffee_maker(coffee_name): # permission to make coffee function
    if is_sufficient(coffee_name) == True:
        print("Please pay first.")
        making_coffee(coffee_name)
        time.sleep(5)
        os.system('clear')
        working()
    elif is_sufficient(coffee_name) == False:
        print(f"Sorry. Shortage of ingredients for your coffee {coffee_name}.")
 
#************************************************* functions **************************************************


#************************************************* main code **************************************************
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

#************************************************* main code **************************************************