import random
from datagame import data



#2 randomo objects

def object_generator():
    random_dict = data[random.randint(0, len(data) - 1)]
    return random_dict


score = 0
def checks(option_A, option_B):
    print(f"Compare A: {option_A['name']}, a {option_A['description']} from {option_A['country']} pssssss following is {option_A['follower_count']}")
    print(f"Against B: {option_B['name']}, a {option_B['description']} from {option_B['country']} pssssss following is {option_B['follower_count']}")
    global score
    answer = input("A or B has more following?: ").casefold()
    if answer == "a":
        if option_A["follower_count"] > option_B["follower_count"]:
            score+=1
            new_option_B = object_generator()
            checks(option_A, new_option_B)
        else:
            print(f"Game over, you are wrong, Your score is {score}")

    elif answer == "b":
        if option_B["follower_count"] > option_A["follower_count"]:
            score+=1
            new_option_A = object_generator()
            checks(option_B, new_option_A)
        else:
            print(f"Game over, you are wrong, Your score is {score}")



#A
option_A = object_generator()
follower_count_A = option_A["follower_count"]


#B
option_B = object_generator()
follower_count_B = option_B["follower_count"]

checks(option_A, option_B)





