# hangman game
import random

words = ["hello", "cat", "mouse", "dog", "laptop", "football"]
random_word = random.choice(words)
print(random_word)

blank = ""
for i in range(len(random_word)):
    blank += "_"
print(blank)

game_over = False

previous_value_store = []

while not game_over:

    display = ""
    guess = input("Guess a letter: ").lower()
    for letter in random_word:
        if letter == guess:
            display += letter
            previous_value_store += letter
        elif letter in previous_value_store:
            display += letter
        else:
            display += "_"

    if "_" not in display:
        print("You win")
        game_over = True

    print(display)

