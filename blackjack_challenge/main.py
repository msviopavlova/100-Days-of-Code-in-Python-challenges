import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []


#this function deals a card to whoever player is passed as a parameter and adds the card to their hand
def deal_card(whom):
    random_card = random.choice(cards)
    whom.append(random_card)
    return random_card


# this for loop adds 2 card to each player in the beginning of the game
for call in range(2):
    deal_card(user_cards)
    deal_card(computer_cards)


score_sum_user = sum(user_cards)
score_sum_computer = sum(computer_cards)

def calculate_score(who):
    score = sum(who)
    if score == 21:
        return f"{who} has a Blackjack and wins!"
    elif score > 21:
        print(who)
        print("game over we are over 21")
        #another_card = input(f"your score is {score} Would you like another card? 'y' or 'n': ")
        #if another_card == "y":
        #  deal_card(who)
        #  print(f"we are inside over 21 ad {who}")
    else:
        another_card = input(f"your score is {score} Would you like another card? 'y' or 'n': ")
        if another_card == "y":
            deal_card(who)
            calculate_score(who)
        









   

#calling and calculating both scores 
current_user_score = calculate_score(user_cards)
#current_computer_score = calculate_score(computer_cards)



























































