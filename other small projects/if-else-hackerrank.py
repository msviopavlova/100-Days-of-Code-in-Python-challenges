n = int(input())


if (n % 2 == 1) or (n in range(6, 21) and n % 2 == 0):
    print("Weird")
elif (n in range(2, 6) and n % 2 == 0)  or (n in range(6, 21) and n % 2 == 0) or (n % 2 == 0 and n > 20) :
    print("Not Weird")

