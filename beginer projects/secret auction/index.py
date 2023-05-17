import os

bidders = []

def bidders_info(name, amount):
    new_bidder = {}
    new_bidder["name"] = name
    new_bidder["amount"] = amount

    bidders.append(new_bidder)

# bidders_info("deku", 10)
# print(bidders)

while True:
    user_name = input("Enter your name: ").strip()
    bid_amount = int(input("Enter your bidding amount:$ ").strip())

    bidders_info(user_name, bid_amount)

    user_que = input("if there are other members to bid type \'yes\' otherwise type \'no\': ").strip()

    if user_que == "yes":
        os.system('clear')
        continue
    else:
        break

winner = max(bidders, key= lambda item: item.get("amount"))["name"]
print(f"the winner is {winner}!!!")


    
