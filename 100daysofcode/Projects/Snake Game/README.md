# Snake Game

A classic Snake game implemented in Python using the `turtle` graphics library.

## Features

- Adjustable difficulty (Normal, Fast, Fastest)
- Pause (`p`), Restart (`r`), and Quit (`q`) controls
- Edge wrapping (snake appears on the opposite side)
- Persistent high score saved to `high_score.txt`
- "Game Over" and "Paused" messages
- Scoreboard display

## Controls

- **W**: Move Up
- **S**: Move Down
- **A**: Move Left
- **D**: Move Right
- **P**: Pause/Unpause
- **R**: Restart Game
- **Q**: Quit Game

## How to Play

1. Run `main.py`:
    ```
    python main.py
    ```
2. Choose a difficulty when prompted.
3. Use the controls to move the snake and eat the blue food.
4. Avoid colliding with your own tail.
5. Try to beat your high score!

## Files

- `main.py` - Main game loop and event handling
- `snake.py` - Snake logic and movement
- `food.py` - Food spawning logic
- `scoreboard.py` - Score and high score management

## Requirements

- Python 3.x
- `turtle` module (included with standard Python)

---

Enjoy the
