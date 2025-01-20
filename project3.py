print('''
*************
      ***********
            **********
                 *****************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

step1 = input("you are at a cross road. where do you want to go? Type 'left' or 'right'\n").lower()

if step1 == "right":
    step2 = input("Do you want to wait for boat or swim? Type \"wait\" or \"swim\"\n").lower()
    if step2 == "wait":
        print("you have reached the island smoothly")
        step3 = input("choose 1 door: 'yellow', 'red', 'blue'\n").lower()
        if step3 == "yellow":
            print("you found the treasure. Congratulations.")
        else:
            print("you chose the wrong door. Game over.")
    else:
        print("Crocodiles everywhere. Game Over.")
else: 
    print("You fell in a hole. Game over.")
