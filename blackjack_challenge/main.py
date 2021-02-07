import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []


#this function deals a card to whoever player is passed as a parameter and adds the card to their hand
def deal_card(current_player):
    random_card = random.choice(cards)
    current_player.append(random_card)
    return random_card


# this for loop adds 2 card to each player in the beginning of the game
for call in range(2):
    deal_card(user_cards)
    deal_card(computer_cards)


score_sum_user = sum(user_cards)
score_sum_computer = sum(computer_cards)

def calculate_score(player):
    score = sum(player)
    return score



def blackjack(player):
    current_score = calculate_score(player)
    if current_score == 21:
        return f"{player} has a Blackjack and wins!"
    elif current_score > 21:
        print(player)
        print("game over we are over 21")
    else:
        another_card = input(f"your score is {current_score} Would you like another card? 'y' or 'n': ")
        if another_card == "y":
            deal_card(player)
            blackjack(player)



        


blackjack(user_cards)






























































