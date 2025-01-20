# strong password generator

letters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = [
    "+", "-", "*", "/", "%", "<", ">", "&", "|", "^", "~", "=", "\\",
    "@", "#", "$", "_", ".", ",", ";", ":", "'", "\"", "?", "!", "(", 
    ")", "[", "]", "{", "}"
]

print("Welcome to Python Password Generator!")
num_of_letters = int(input("How many letters do you want?\n"))
num_of_numbers = int(input("How many numbers do you want?\n"))
num_of_symbols = int(input("How many symbols do you want?\n"))

# easy way
import random

password = ""

for letter in range(0, num_of_letters):
    password += random.choice(letters)

for number in range(0, num_of_numbers):
    password += random.choice(numbers)

for symbol in range(0, num_of_symbols):
    password += random.choice(symbols)

print(f"Easy Password: {password}")

# hard way
hard_password = ""
password_as_list = []
length = len(password)

for i in range(0, length):
    char = password[i]
    password_as_list.append(char)

# print(password_as_list)

for i in range(0, length):
    rand = random.choice(password_as_list)
    password_as_list.remove(rand)
    hard_password += rand

print(f"Hard Password: {hard_password}")