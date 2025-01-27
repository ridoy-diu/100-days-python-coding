import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw."
    elif u_score == 0:
        return "Win with a blackjack."
    elif c_score == 0:
        return "Lose, computer has a blackjack."
    elif u_score > 21:
        return "Lose, you went over."
    elif c_score > 21:
        return "Win, computer went over."
    elif u_score > c_score:
        return "You Win."
    else:
        return "You Lose."


def play():

    player_cards = []
    player_score = -1
    computer_cards = []
    computer_score = -1
    gameover = False

    for i in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not gameover:

        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            gameover = True
        else:
            get_another_card = input("Type 'y' to get another card, type 'n' to pass:")
            if get_another_card == 'y':
                player_cards.append(deal_card())
            else:
                gameover = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))

while input("Do you want to play Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 50)
    play()