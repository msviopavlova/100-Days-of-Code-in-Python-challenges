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


def generator():
   pass
    #new_option = data[random.randint(0, len(data) - 1)



print(f"Compare A: {name_A}, a {description_A} from {country_A}")
print(f"Against B: {name_B}, a {description_B} from {country_B}")



def compare(your_answer, against):
    if your_answer > against:
        return f"Your answer was {your_answer}, it is greater than {against} indeed"
    elif your_answer > against:
        return f"Your answer is wrong because {your_answer} is less than {against} "

answer = input("Please type A or B: ").casefold()
if answer == "a":
    print(compare(follower_count_A, follower_count_B))
elif answer == "b":
    print(compare(follower_count_B, follower_count_A))








