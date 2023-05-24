print("welcome to tip calculator!")
total_bill = int(input("What was the total bill? ").strip())
num_people = int(input("How many people do you want to split the bill into? ").strip())
percentage_of_bill = int(input("How much tip you want to give? 10 or 12 or 15% ? please just write the amount not the \'%\' sign ").strip())

bill_with_tip = total_bill + (total_bill*percentage_of_bill/100)
indivisual_bill = bill_with_tip/num_people

print(f"the bill is ${indivisual_bill: .2f} per person")
