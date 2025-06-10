# from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
def black_jeck():
    if start == 'y':
        # print(logo)
        player_cards = random.sample(cards, 2)
        player_score = sum(player_cards)
        cpu_cards = random.sample(cards, 2)
        print(f"Your card: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {cpu_cards[0]}")
    else:
        print("you enter 'n' game will be closed")
        return
    while player_score < 21:
        new_card = input(f"Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if new_card == 'y':
            player_card_new = random.choice(cards)
            player_cards.append(player_card_new)
            player_score = sum(player_cards)
            print(f"Your card: {player_cards}, current score: {player_score}")
            print(f"Computer's first card: {cpu_cards[0]}")
        elif player_score > 21:
            print(f"Your final hand: {player_cards}, final score: {player_score}")
            print(f"You went over with {player_score}. You lose!")
            break
        else:
            break
black_jeck()