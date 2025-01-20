# rock, paper, scissors game with computer

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

option = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor.\n"))

if user_choice < 0 or user_choice >= 3:
    print("Invalid choice")
else:
    print("You chose:")
    print(option[user_choice])
    
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(option[computer_choice])
    
    if user_choice == computer_choice:
        print("It's a Draw!")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("You Win!")
    else:
        print("You Lose!")


# will update the game after learning loop
# update - first to score 5 points will win