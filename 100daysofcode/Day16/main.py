from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True
while True:
    # Display the menu and prompt the user for their choice
    print("Welcome to the Coffee Machine!")
    print("Here is the menu:")
    choice = input(f" ({menu.get_items()}): ").lower()
    if choice == "off":
        is_on = False
        print("Turning off the coffee machine. Goodbye!")
        break
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # Check if the choice is valid
        drink = menu.find_drink(choice)
        if drink is None:
            print("Sorry, that item is not on the menu.")
            continue

        # Check if resources are sufficient
        if not coffee_maker.is_resource_sufficient(drink):
            print("Sorry, there are not enough resources to make that drink.")
            print("Here is the menu:")
            choice = input(f" ({menu.get_items()}): ").lower()
            continue

        # Process payment
        if money_machine.make_payment(drink.cost):
            # Make the coffee
            coffee_maker.make_coffee(drink)
