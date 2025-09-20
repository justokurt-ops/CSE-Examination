def gps_tracker():
    x = 0
    y = 0
    print("Start at (0,0)")

    while True:
        move = input("Enter N/S/E/W or STOP: ").lower()

        if move == "stop":
            break
        elif move == "n" or move == "north":
            y += 1
        elif move == "s" or move == "south":
            y -= 1
        elif move == "e" or move == "east":
            x += 1
        elif move == "w" or move == "west":
            x -= 1
        else:
            print("Invalid input!")
            continue

        print("Current position:", (x, y))

    print("Final position:", (x, y))
    if x == 0 and y == 0:
        print("You returned to the origin.")
    else:
        print("You did not return to the origin.")

gps_tracker()
