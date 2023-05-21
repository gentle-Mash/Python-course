def total_amount(): # money processing function
    
    q = int(input("How many quarters: ").strip()) * 0.25
    d = int(input("How many dimes: ").strip()) * 0.10
    n = int(input("How many nickles: ").strip()) * 0.05
    p = int(input("How many pennis: ").strip()) * 0.01

    total_price = q + d + n + p
    return total_price


def machine_money_count(dict1,dict2,coffee_name): # keep track of total sell
    dict1["money"] += dict2[coffee_name]["cost"]


def is_sufficient(dict1,dict2,coffee_name): # ingredients checking function
    if (dict1["water"] >= dict2[coffee_name]["ingredients"]["water"]) and (dict1["milk"] >= dict2[coffee_name]["ingredients"]["milk"]) and (dict1["coffee"] >= dict2[coffee_name]["ingredients"]["coffee"]):
        return True
    return False


def making_coffee(dict1,dict2,coffee_name):  # main coffee maker function 
    user_given_amount = total_amount()
    if user_given_amount < dict2[coffee_name]["cost"]:
        print("Sorry. Not enough money. Money refunded")
    elif user_given_amount > dict2[coffee_name]["cost"]:
        change = user_given_amount - dict2[coffee_name]["cost"]
        print(f"Here is your change ${round(change, 3)} and your {coffee_name}.Enjoy!")
        for key in dict1:
            if key != "money":
                dict1[key] = dict1[key] - dict2[coffee_name]["ingredients"][key]
            else:
                machine_money_count(dict1,dict2,coffee_name)


