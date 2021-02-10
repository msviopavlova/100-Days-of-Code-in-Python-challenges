import random
from datagame import data

score = 0
#A = print(Compare A "objects key " , "objects description", "city of the object")

#data[number] gets a dictionary from a list

#this gets Christiano Ronaldo name print(data[1]["name"])

#print(data[]["follower_count"])

#A
option_A = data[random.randint(0, len(data) - 1)]
name_A = option_A["name"]
description_A = option_A["description"]
follower_count_A = option_A["follower_count"]
country_A = option_A["country"]

#B
option_B = data[random.randint(0, len(data) - 1)]
name_B = option_B["name"]
description_B = option_B["description"]
follower_count_B = option_B["follower_count"]
country_B = option_B["country"]


print(f"Compare A: {name_A}, a {description_A} from {country_A} pssssss following is {follower_count_A}")
print(f"Against B: {name_B}, a {description_B} from {country_B} pssssss following is {follower_count_B}")
answer = input("Please type A or B: ").casefold()

def compare(your_answer, against):
    if your_answer > against:
        print(f"Your answer was {your_answer}, it is greater than {against} indeed")
        return 1
    elif your_answer < against:
        print(f"Your answer is wrong because {your_answer} is less than {against} ")
        return 0

def choice(your_choice):
    if your_choice == "a":
        if compare(follower_count_A, follower_count_B) == 1:
            print("We are inside 1 is true statement a vs b")
            return
        elif compare(follower_count_A, follower_count_B) == 0:
            print("We are inside a vs b and we are wrong return was 0")
    elif your_choice == "b":
        if compare(follower_count_B, follower_count_A) == 1:
            print("inside b vs a is true = 1 ")
        elif compare(follower_count_B, follower_count_A) == 0:
            print("inside be but return was 0 we are wrong ")

choice(answer)









