# caesear cipher

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

def encode_or_decode(message, shift_amount, choice):

    if choice == "decode":
        shift_amount *= -1

    new_message = ""
    for letter in message:
        if letter not in alphabet:
            new_message += letter
            continue

        shift_position = alphabet.index(letter) + shift_amount
        shift_position %= len(alphabet) # range 0 - 25
        new_message += alphabet[shift_position]

    print(f"The {choice}d message:", new_message)

should_continue = False
while not should_continue:
    choice = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()

    if choice == "encode" or choice == "decode":
        message = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encode_or_decode(message, shift, choice)
    else:
        print("Invalid. Run again.")
        exit()

    yes_or_no = input("Do you want to continue? Type 'yes' or 'no'\n").lower()
    if yes_or_no == "no":
        should_continue = True
        print("goodbye")




# def encrypt(message, shift):
#     encrypted_message = ""
#     for letter in message:
#         if letter not in alphabet:
#             continue
#         shift_position = alphabet.index(letter) + shift
#         shift_position %= len(alphabet) # range 0 - 25
#         encrypted_message += alphabet[shift_position]
#     print("The encrypted message:", encrypted_message)
# def decrypt(message, shift):
#     decrypted_message = ""
#     for letter in message:
#         if letter not in alphabet:
#             continue
#         shift_position = alphabet.index(letter) - shift
#         decrypted_message += alphabet[shift_position]
#     print("The decrypted message:", decrypted_message)