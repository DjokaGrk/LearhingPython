from data import resources, MENU

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
# TODO:  1. promt user for input “What would you like? (espresso/latte/cappuccino):”
print("Welcome to the Coffee Machine!")


def get_user_choice():
    """
    Prompts the user for their coffee choice.

    Returns:
        str: The user's choice of coffee.
    """
    return input("What would you like? (espresso/latte/cappuccino): ").lower()


# TODO:  2. secret code to turn off the machine
def check_secret_code():
    """
    Checks if the user has entered the secret code to turn off the machine.

    Returns:
        bool: True if the secret code is entered, False otherwise.
    """
    return input("Enter the secret code to turn off the machine: ") == "off"


# TODO:  3. check resources with "report"
def check_resources(choice):
    """
    Checks if there are enough resources for the selected drink.

    Args:
        choice (str): The drink selected by the user.

    Returns:
        bool: True if resources are sufficient, False otherwise.
    """
    # TODO:  4. check if resources are sufficient
    ingredients = MENU[choice]["ingredients"]
    if water < ingredients.get("water", 0):
        print("Sorry, not enough water.")
        return False
    if milk < ingredients.get("milk", 0):
        print("Sorry, not enough milk.")
        return False
    if coffee < ingredients.get("coffee", 0):
        print("Sorry, not enough coffee.")
        return False
    return True


# TODO:  5. process coins
def process_coins():
    """
    Processes the coins inserted by the user.

    Returns:
        float: The total amount of money inserted.
    """
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    money_inserted = quarters + dimes + nickels + pennies
    print(f"Total money inserted: ${money_inserted:.2f}")
    if money_inserted < MENU[choice]["cost"]:
        print("Sorry, not enough money. Please insert more coins.")
        return process_coins()
    elif money_inserted > MENU[choice]["cost"]:
        change = money_inserted - MENU[choice]["cost"]
        print(f"Here is your {choice}. Enjoy!")
        print(f"Here is your change: ${change:.2f}")
    return quarters + dimes + nickels + pennies


# Main loop to handle user input and coffee preparation
while True:
    choice = get_user_choice()
    if choice == "off":
        check_secret_code()
        print("Turning off the machine. Goodbye!")
        break
    elif choice == "report":
        print("Water:", water, "ml")
        print("Milk:", milk, "ml")
        print("Coffee:", coffee, "g")
        print("Money: $0.00")
    # TODO:  6. make coffee
    elif choice in MENU:
        if check_resources(choice):
            water -= MENU[choice]["ingredients"].get("water", 0)
            coffee -= MENU[choice]["ingredients"].get("coffee", 0)
            milk -= MENU[choice]["ingredients"].get("milk", 0)
            print(f"{choice.capitalize()} is being prepared.")
            cost = MENU[choice]["cost"]
            inserted_money = process_coins()

    else:
        print("Invalid choice. Please try again.")
