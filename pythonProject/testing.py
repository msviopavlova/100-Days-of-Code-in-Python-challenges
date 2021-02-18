list = [125, 50, 1, -10, -50]
positive_numbers = []
negative_number = []
for i in list:

#    if its over 0 then its positive
#    find the minim one and return it
#
#
#    if its less than 0 then its negative
#    find the maximum one and return it
    if i > 0 :
        print("This number is positive")
        positive_numbers.append(i)
    elif i < 0:
        print("This number is negative")
        negative_number.append(i)

lowest_from_positive = min(positive_numbers)
highest_from_negative = max(negative_number)

# making the negative number a positive one and then comparing them

new_positive = -highest_from_negative

if new_positive > lowest_from_positive:
    print(f"lowest from positive is closer to 0  = {lowest_from_positive} because negative was {highest_from_negative}")
elif new_positive < lowest_from_positive:
    print(f"the negative one ({highest_from_negative}) is closer to 0 than {lowest_from_positive}")