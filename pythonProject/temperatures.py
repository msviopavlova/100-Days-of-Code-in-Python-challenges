import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
zero = 0

list_of_temps = []
#n = int(input())



# the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    list_of_temps.append(t)
#lowest_temp = min(list_of_temps)



# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(lowest_temp)
