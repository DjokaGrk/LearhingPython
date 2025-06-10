# from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
def blackJeck():
    if start == 'y':
        # print(logo)
        player_cards = random.sample(cards, 2)
        player_score = sum(player_cards)
        cpu_cards = random.sample(cards, 2)
        print(f"Your card: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {cpu_cards[0]}")
    else:
        print("you enter 'n' game will be closed")