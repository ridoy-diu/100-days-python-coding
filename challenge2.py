print("Welcome to Python pizza deliveries")

bill = 0

size = input("what size pizza do you want? Small(S), Medium(M) or Large(L)?\n").upper()
if size == "S" or size == "M" or size == "L":
    pepperoni = input("do you want pepperoni on your pizza? Yes(Y) or No(N)?\n").upper()
    if pepperoni == "Y" or pepperoni == "N":
        extra_cheese = input("do you want extra cheese on your pizza? Yes(Y) or No(N)?\n").upper()
        if extra_cheese != "Y" or extra_cheese != "N": 
            print("Invalid input for extra cheese.")
            exit() 
    else:
        print("Invalid input for pepperoni.") 
        exit()
else:
    print("Invalid input for size.") 
    exit()   



if size == "S":
    bill = 349
    if pepperoni == "Y":
        bill += 100
    if extra_cheese == "Y":
        bill += 40
elif size == "M":
    bill = 799
    if pepperoni == "Y":
        bill += 150
    if extra_cheese == "Y":
        bill += 50
else:
    bill = 1099
    if pepperoni == "Y":
        bill += 180
    if extra_cheese == "Y":
        bill += 60

print("Your final bill is " + str(bill))