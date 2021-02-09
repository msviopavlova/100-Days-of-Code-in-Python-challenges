import random
from datagame import data

score = 0
#A = print(Compare A "objects key " , "objects description", "city of the object")

#data[number] gets a dictionary from a list

#this gets Christiano Ronaldo name print(data[1]["name"])

#print(data[]["follower_count"])



def compare(your_answer, against):
    if your_answer > against:
        print(f"Your answer was {your_answer}, it is greater than {against} indeed")
        return 1
    elif your_answer < against:
        print(f"Your answer is wrong because {your_answer} is less than {against} ")
        return 0




def generate_options():
    random_dict = data[random.randint(0, len(data) - 1)]
    return random_dict



def choice(your_choice):
    """checks whether A or B."""
    if your_choice == "a":
        if compare(follower_count_A, follower_count_B) == 1:
           #case where user is right
            #call some function that will create a new option and save this one
            current_object = option_A
            return current_object
        else:
            return 0
    elif your_choice == "b":
        if compare(follower_count_B, follower_count_A) == 1:
            #case where user is right
            current_object = option_B
            return current_object
        else:
            return 0
    else:
        print("Invalid option start again")



#A
option_A = generate_options()
name_A = option_A["name"]
description_A = option_A["description"]
follower_count_A = option_A["follower_count"]
country_A = option_A["country"]

#B
option_B = generate_options()
name_B = option_B["name"]
description_B = option_B["description"]
follower_count_B = option_B["follower_count"]
country_B = option_B["country"]

game_goes_on = True
while game_goes_on:

    print(f"Compare A: {name_A}, a {description_A} from {country_A} pssssss following is {follower_count_A}")
    print(f"Against B: {name_B}, a {description_B} from {country_B} pssssss following is {follower_count_B}")

    answer = input("Please type A or B: ").casefold()

    if choice(answer) == 0:
        game_goes_on = False



#dynamicv function that takes out the names and other values from dictionaries and gives than names, to a passed value (maybe data )
