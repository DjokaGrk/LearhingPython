import random
from game_data import letters, numbers, symbols

def generate_password(nr_letters, nr_symbols, nr_numbers):
    """
    Generates a random password based on the number of letters, symbols, and numbers.

    Args:
        nr_letters (int): Number of letters in the password.
        nr_symbols (int): Number of symbols in the password.
        nr_numbers (int): Number of numbers in the password.

    Returns:
        str: The generated password.
    """
    password_list = (
        [random.choice(letters) for _ in range(nr_letters)] +
        [random.choice(symbols) for _ in range(nr_symbols)] +
        [random.choice(numbers) for _ in range(nr_numbers)]
    )
    random.shuffle(password_list)
    return ''.join(password_list)

def main():
    """
    Main function to prompt user input and display the generated password.
    """
    print("Welcome to the Password Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))

    password = generate_password(nr_letters, nr_symbols, nr_numbers)
    print(f"Your password is: {password}")

if __name__ == "__main__":
    main()
