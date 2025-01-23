# hangman game
import random

hangman_art = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ["hello", "cat", "mouse", "dog", "laptop", "football", "cricket", "doctor", "phone"]
random_word = random.choice(words)
# print(random_word)

blank = ""
for i in range(len(random_word)):
    blank += "_"
print(blank)

game_over = False

previous_value_store = []

lives = 6

while not game_over:

    print("You have ", lives, " lives left.")
    display = ""
    guess = input("Guess a letter: ").lower()
    
    if guess not in random_word:
        print(f"You guessed {guess}, which is not in the word. So you lost a life.")
        lives -= 1

    if guess in previous_value_store:
        print(f"You have already guessed {guess}")

    for letter in random_word:

        if letter == guess:
            display += letter
            previous_value_store += letter
        elif letter in previous_value_store:
            display += letter
        else:
            display += "_"

    if "_" not in display:
        print("********You Win!********")
        game_over = True

    if lives == 0:
        print("********You Lose!********")
        print("The correct word was ", random_word)
        game_over = True

    print("\nDISPLAY: ", display)
    print(hangman_art[6 - lives])

