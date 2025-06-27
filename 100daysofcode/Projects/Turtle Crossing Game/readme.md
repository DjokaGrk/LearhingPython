# Turtle Crossing Game

A simple arcade-style game built with Python's `turtle` module. Help the turtle cross the road while avoiding cars!

## How to Play

- Press **W** to move the turtle forward.
- Each time you reach the top, you level up and the cars move faster.
- If the turtle collides with a car, the game ends.

## Features

- Randomly colored cars move from right to left.
- Each level increases the speed of the cars.
- Scoreboard displays your current level.
- "Game Over" message when you lose.

## Requirements

- Python 3.x
- The `turtle` module (comes with standard Python)

## How to Run

1. Download all files in this folder.
2. Run the game with:
    ```
    python main.py
    ```

## File Structure

- `main.py` - Main game loop and event handling
- `player.py` - Player (turtle) logic
- `car_manager.py` - Car creation and movement logic
- `scoreboard.py` - Scoreboard and game over display

---

Enjoy the game and try to reach the highest level!
