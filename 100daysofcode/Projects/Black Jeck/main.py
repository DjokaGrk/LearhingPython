from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(hand):
    """
    Calculates the total score of a hand in Blackjack.
    Converts Ace (11) to 1 if the total score exceeds 21.

    Args:
        hand (list): List of integers representing card values.

    Returns:
        int: The calculated score for the hand.
    """
    score = sum(hand)
    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

def show_hands(player, cpu, hide_cpu=True):
    """
    Displays the player's and computer's cards and scores.

    Args:
        player (list): Player's hand.
        cpu (list): Computer's hand.
        hide_cpu (bool): If True, only shows the computer's first card.
    """
    print(f"Your cards: {player}, current score: {calculate_score(player)}")
    if hide_cpu:
        print(f"Computer's first card: {cpu[0]}")
    else:
        print(f"Cpu final hand: {cpu}, final score: {calculate_score(cpu)}")

def black_jack():
    """
    Main function to run the Blackjack game.
    Handles the game loop, player and dealer turns, and determines the outcome.
    """
    print(logo)
    print("Welcome to Blackjack!")
    while True:
        if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() != 'y':
            print("Thanks for playing!")
            break

        player = [random.choice(cards), random.choice(cards)]
        cpu = [random.choice(cards), random.choice(cards)]
        show_hands(player, cpu)

        # Player turn
        while calculate_score(player) < 21:
            if input("Type 'y' to get another card, 'n' to pass: ").lower() == 'y':
                player.append(random.choice(cards))
                show_hands(player, cpu)
                if calculate_score(player) > 21:
                    print(f"You went over with {calculate_score(player)}. You lose!")
                    break
            else:
                break

        # Dealer turn
        while calculate_score(cpu) < 17:
            cpu.append(random.choice(cards))

        show_hands(player, cpu, hide_cpu=False)
        player_score = calculate_score(player)
        cpu_score = calculate_score(cpu)

        if player_score > 21:
            print("You went over. You lose!")
        elif cpu_score > 21 or player_score > cpu_score:
            print("You win!")
        elif player_score < cpu_score:
            print("You lose!")
        else:
            print("Draw!")

black_jack()
