# Tip Calculator

print("Welcome to the Tip Calculator")

bill = float(input("Your bill? BDT "))
tip = float(input("How much tip do you want to give(in %)?\n"))
person = int(input("How many person to split the bill?\n"))

tip_amount = bill * (tip / 100)
bill_with_tip = bill + tip_amount
per_person_bill = bill_with_tip/person

print(f"Your tip is {round(tip_amount, 2)}")
print(f"Your bill with tip is {round(bill_with_tip, 2)} BDT")
print(f"Each person should pay: {round(per_person_bill, 2)} BDT")

