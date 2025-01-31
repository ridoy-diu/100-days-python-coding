import random

print("Welcome to number guessing game.\n  I am thinking of a number between 1 and 100.\n")
random_number = random.randint(0, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = 10
if difficulty == "hard":
    attempts = 5

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess_number = int(input("Make a guess: "))
    if guess_number == random_number:
        print("The number is " + str(guess_number))
        print("YOU WIN\n")
        attempts = 0
    else:
        if guess_number > random_number:
            print("Too high. Guess again\n")
            attempts -= 1
        else:
            print("Too low. Guess again\n")
            attempts -= 1

    if attempts == 0:
        print("You are out of guesses, YOU LOSE\n")
        print("The number is " + str(guess_number))