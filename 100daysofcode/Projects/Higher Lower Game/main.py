from game_data import data
import random
from art import logo, vs

def get_random_data():
    """
    Returns a random item from the data list.

    Returns:
        dict: A randomly selected dictionary from the data list.
    """
    return random.choice(data)

while True:
    """
    Main game loop for the Higher Lower Game.
    Displays the logo, manages the score, and handles replay logic.
    """
    print(logo)
    score = 0
    game_continue = True
    item_a = get_random_data()
    item_b = get_random_data()

    while game_continue:
        """
        Inner game loop for each comparison round.
        Swaps items, ensures uniqueness, and checks the player's guess.
        """
        item_a, item_b = item_b, get_random_data()
        while item_a == item_b:
            item_b = get_random_data()

        print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}.")
        print(vs)
        print(f"Against B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}.")

        choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        if (choice == 'A' and item_a['follower_count'] > item_b['follower_count']) or \
           (choice == 'B' and item_b['follower_count'] > item_a['follower_count']):
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_continue = False
            print(f"Sorry, that's wrong. Final score: {score}.")

    if input("Do you want to play again? Type 'y' or 'n': ").lower() != 'y':
        print("Thanks for playing!")
        break




