print("welcome to the rollercoaster")

height = int(input("Your height in cm? "))
bill = 0
person = ""

if height < 120 :
    print("can not ride")
else :
    print("can ride")
    age = int(input("Your age?\n"))
    if age <= 12: 
        bill = 50
        person = "child"
    elif 13 <= age < 18: # age >= 13 and age < 18
        bill = 75
        person = "youth"
    else : 
        bill = 100
        person = "adult"
    
    want_photo = input("do you want photo? type 'y' for yes, 'n' for no\n")
    if want_photo == "Y":
        print("30 tk for photo")
        print(f"You are a {person}, Fees = {bill} tk")
        print(f"Your bill with photo is {bill + 30} tk")
    else : 
        print(f"You are a {person} so you have to pay {bill} tk")


# --------------------------------------------
# odd or even
num = int(input("Enter a number: "))
if num % 2 == 0: print("even")
else: print("odd")