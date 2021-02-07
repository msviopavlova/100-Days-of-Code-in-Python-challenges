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

#adding up both scores
score_sum_user = sum(user_cards)
score_sum_computer = sum(computer_cards)

#checking if blackjack

blackjack = 21

if score_sum_user == blackjack:
    print(f"your current score is {score_sum_user} Blackjack! You won!")
    #terminate game with a flag and start again
elif score_sum_computer == blackjack:
    print(f"Computer's score is {score_sum_computer} and yours score is {score_sum_user} - YOU LOSE! =(((")
    #terminate game with a flag  and start again









print(user_cards)
print(computer_cards)











def calculate_score():
    pass
    #return sum(user_cards)