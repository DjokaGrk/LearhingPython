import random
from game_data import rock, paper, scissors
choice = int(
    input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors.\n")
)
choices = [rock, paper, scissors]
if choice < 0 or choice >= 3:
    print("invalid number , try again")
else:
    cpu_choice = random.randint(0, 2)
    print(f"\nyou choose\n{choices[choice]}")
    print(f"\ncpu choose\n{choices[cpu_choice]}")
    # ko pobedjuje
    if choice == cpu_choice:
        print("its a draw")
    elif (
        (choice == 0 and cpu_choice == 2)
        or (choice == 1 and cpu_choice == 0)
        or (choice == 2 and cpu_choice == 1)
    ):
        print("you win")
    else:
        print("you lose")
