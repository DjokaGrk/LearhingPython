def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
        if right_is_clear():
            turn_right()
        elif front_is_clear():
             move()
        else:
             turn_left()
    elif wall_in_front():
        turn_right()
    else:
        move()
