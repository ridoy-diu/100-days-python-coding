# Blackjack Game
import random

def calculate_score(card_list):
    score = 0
    for card in card_list:
        score += card
    return score

def get_random_card(card_list):
    card = random.choice(card_list)
    card_list.remove(card)
    return card


human_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_cards = human_cards

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")

card1 = get_random_card(human_cards)
card2 = get_random_card(human_cards)
computercard1 = get_random_card(computer_cards)
computercard2 = get_random_card(computer_cards)
current_cards = [card1, card2]
current_computer_cards = [computercard1, computercard2]

print(f"Your cards: {current_cards}, current score: {calculate_score(current_cards)}")
print(f"Computer's first card: {computercard1}")


get_another_card = input("Type 'y' to get another card, type 'n' to pass:")
if get_another_card == 'y':
    card_n = random.choice(human_cards)
    current_cards.append(card_n)

print(f"Your final hand: {current_cards}, final score: {calculate_score(current_cards)}")
print(f"Computer's final hand: {current_computer_cards}, final score: {calculate_score(current_computer_cards)}")