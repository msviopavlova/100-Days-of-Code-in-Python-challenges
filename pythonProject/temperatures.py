import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
positive_numbers = []
negative_number = []

list = []

n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    list.append(t)
if list == []:
    print(0)
else:
    for i in list:
        if i > 0:
            # print("This number is positive")
            positive_numbers.append(i)
        elif i < 0:
            # print("This number is negative")
            negative_number.append(i)

    if positive_numbers != []:
        lowest_from_positive = min(positive_numbers)
        highest_from_negative = max(negative_number)

        # making the negative number a positive one and then comparing them

        new_positive = -highest_from_negative
        if new_positive == lowest_from_positive:
            print(lowest_from_positive)
        elif new_positive > lowest_from_positive:
            print(lowest_from_positive)
        elif new_positive < lowest_from_positive:
            print(highest_from_negative)
    else:
        highest_from_negative = max(negative_number)
        print(highest_from_negative)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


