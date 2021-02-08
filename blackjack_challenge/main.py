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


# score_sum_user = sum(user_cards)
# score_sum_computer = sum(computer_cards)

def calculate_score(player):
    score = sum(player)
    #print(f"currently your score is {score} with a hand of  {player}")
    if score == 21:
        print(f"user {player} has a Blackjack and wins!")
        return score
    elif score > 21:
        print(f"User score over 21")
        return score
    else:
        another_card = input(f"your score is {score} Would you like another card? 'y' or 'n': ")
        if another_card == "y":
            deal_card(player)
            calculate_score(player) #TODO had an issue with return statement here, removed it

        elif another_card == "n":
            return sum(player)



user_score = calculate_score(user_cards)
print(f"user score variable was {user_score}")


#a function for counting the computer score

def computer_calculate(dealer_hand):
    dealer_score = sum(dealer_hand)
    print(f"computer score  LOOP is {dealer_score} with a hand of {dealer_hand}") # TODO show only first card from computer hand later
    if dealer_score == 21:
        print(f"dealer score is {dealer_score} with hand {dealer_hand} is a Blackjack and Computer should win")
        return dealer_score
    elif dealer_score<21 and len(dealer_hand)<=3:
        deal_card(dealer_hand)

        final_hand = sum(dealer_hand)
        return final_hand
    elif dealer_score > 21:
        print(f"notice that dealer score went over 21 and is {dealer_score}")
        return dealer_score

computer_score = computer_calculate(computer_cards)
print(f"computer score variable was {computer_score}")


def compare(user, computer):
    if user > 21:
        return f"Your Score is {user}, over 21 and Voce Perdeu"
    if computer > 21:
        return f"Computer score is over 21, it is {computer}, You win with a score of {user}!"
    elif computer == 21 and user == 21:
        return f"computer wins, bother user and computer got blackjack"
    elif computer == 21:
        return f"Computer wins with a Blackjack of {computer} and user score is {user}"
    elif user == 21:
        return f"User wins with a score of {user}"
    elif user > computer:
        return f"{user} user wins!"
    elif user < computer:
        return f"{computer} computer wins!"
    elif user == computer:
        return f"Draw, computer score = {computer}, user score = {user}"

final_result = compare(user_score, computer_score)

print(final_result)



































































