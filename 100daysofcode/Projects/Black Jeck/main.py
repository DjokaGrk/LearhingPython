from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(cards_list):
    score = sum(cards_list)
    # Adjust Ace from 11 to 1 if score is over 21
    while score > 21 and 11 in cards_list:
        cards_list[cards_list.index(11)] = 1
        score = sum(cards_list)
    return score

def black_jack():
    print(logo)
    print("Welcome to Blackjack!")
    while True:
        start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if start != 'y':
            print("You entered 'n'. Game will be closed.")
            break

        player_cards = [random.choice(cards), random.choice(cards)]
        cpu_cards = [random.choice(cards), random.choice(cards)]
        player_score = calculate_score(player_cards)
        cpu_score = calculate_score(cpu_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {cpu_cards[0]}")

        while player_score < 21:
            new_card = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if new_card == 'y':
                player_cards.append(random.choice(cards))
                player_score = calculate_score(player_cards)
                print(f"Your cards: {player_cards}, current score: {player_score}")
                if player_score > 21:
                    print(f"You went over with {player_score}. You lose!")
                    break
            else:
                break

        # Dealer logic: draw until 17 or more
        cpu_score = calculate_score(cpu_cards)
        while cpu_score < 17:
            cpu_cards.append(random.choice(cards))
            cpu_score = calculate_score(cpu_cards)

        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Cpu final hand: {cpu_cards}, final score: {cpu_score}")

        if player_score > 21:
            print("You went over. You lose!")
        elif cpu_score > 21 or player_score > cpu_score:
            print("You win!")
        elif player_score < cpu_score:
            print("You lose!")
        else:
            print("Draw!")

        play_again = input("Do you want to play another game? Type 'y' or 'n': ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

black_jack()