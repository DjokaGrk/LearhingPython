# Coffee Machine (OOP)

This project is a Python-based simulation of a coffee machine, implemented using Object-Oriented Programming (OOP) principles.

## About The Project

The primary goal of this project is to apply OOP concepts to create a more structured and maintainable version of a coffee machine program. The machine can brew different types of coffee, manages its resources (water, milk, coffee), and handles monetary transactions.

## Features

*   **Resource Management:** The machine keeps track of its internal resources (water, milk, coffee beans) and will not brew a drink if it lacks the necessary ingredients.
*   **Transaction Processing:** The machine accepts virtual coins, calculates the total, and provides change.
*   **Menu:** The machine offers a menu of drinks, each with a specific recipe and cost.
*   **Reporting:** Users can generate a report to check the current resource levels and the total money earned.

## How to Run

To run the coffee machine simulation, execute the `main.py` file from your terminal:

```bash
python main.py
```

You will be prompted to choose a drink from the menu. You can also type `report` to see the machine's status or `off` to exit the program.

## Project Structure

The project is organized into four main Python files, each representing a distinct class:

*   `main.py`: This is the entry point of the application. It creates instances of the other classes and contains the main loop that drives the machine's operation.
*   `menu.py`: This file defines the `Menu` and `MenuItem` classes, which are responsible for managing the available drinks and their recipes.
*   `coffee_maker.py`: This file contains the `CoffeeMaker` class, which handles the brewing process and manages the machine's resources.
*   `money_machine.py`: This file defines the `MoneyMachine` class, which is responsible for handling all monetary transactions, including processing coins and making change.
