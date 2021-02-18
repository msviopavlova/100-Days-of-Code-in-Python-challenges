import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.
all_mountains = []
highest_mountain = 0

# game loop
while True:
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        all_mountains.append(mountain_h)
    for mountain in all_mountains:
        if mountain > highest_mountain:
            highest_mountain = mountain
            current_index = all_mountains.index(mountain)

        # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # The index of the mountain to fire on.

    print(current_index)
