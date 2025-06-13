# Blackjack (Black Jack) - Python Project

## Game Rules

- **Goal:** Get as close to 21 as possible without going over. Beat the dealer's (CPU) score to win.
- **Card Values:**
  - Number cards (2-10): Face value.
  - Face cards (J, Q, K): 10 points each.
  - Ace (A): 11 points, but counts as 1 if your total would go over 21.
- **Gameplay:**
  1. Both player and dealer are dealt two cards.
  2. Player sees both their cards and one of the dealer's cards.
  3. Player can choose to "Hit" (draw another card) or "Stand" (end their turn).
  4. If the player's total goes over 21, they bust and lose.
  5. After the player stands, the dealer draws cards until reaching at least 17.
  6. If the dealer busts (goes over 21), the player wins.
  7. If neither busts, the higher score wins. If scores are equal, it's a draw.

## How to Play

1. Run `main.py`.
2. Follow the prompts in the terminal:
   - Type `'y'` to play or draw another card.
   - Type `'n'` to stand or exit.
3. The game will display your cards, the dealer's cards, and the result.

## Features

- Handles Ace as 11 or 1 automatically.
- Dealer (CPU) follows standard Blackjack rules.
- Clear win/lose/draw messages.
- Play multiple rounds in one session.

---

Enjoy the game!