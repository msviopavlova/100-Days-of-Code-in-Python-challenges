import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []


#this function deals a card to whoever player is passed as a parameter and adds the card to their hand
def deal_card(whom):
    random_card = random.choice(cards)
    whom.append(random_card)


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
        # make the game false and stop
        # call the mail game function to ask again 
    return score


current_user_score = calculate_score(user_cards)
current_computer_score = calculate_score(computer_cards)


































print(user_cards)
print(computer_cards)













