from art import logo
import random

def thinking_number():
    """
    Main function to run the number guessing game.
hard    Handles difficulty selection, guessing loop, win/lose logic, and restart option.
    """
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = get_attempts(difficulty)

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = get_guess()
        if guess == secret_number:
            print(f"You got it! The answer was {secret_number}.")
            return
        elif guess > secret_number:
            print("Too high.")
        else:
            print("Too low.")
        attempts -= 1

    print(f"You've run out of attempts. The number was {secret_number}.")
    restart = input("Do you want to restart the game? Type 'y' for yes or 'n' for no: ").lower()
    if restart == 'y':
        thinking_number()
    else:
        print("Thank you for playing the game")

def get_attempts(difficulty):
    """
    Returns the number of attempts based on the chosen difficulty.

    Args:
        difficulty (str): The difficulty level chosen by the user.

    Returns:
        int: Number of attempts allowed.
    """
    return 10 if difficulty == 'easy' else 5

def get_guess():
    """
    Prompts the user to enter a guess and returns it as an integer.

    Returns:
        int: The user's guessed number.
    """
    return int(input("Make a guess: "))

thinking_number()
