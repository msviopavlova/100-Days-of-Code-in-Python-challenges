
def new_bid(name, bet):
    bid_bet = int(bet)
    new_person[name] = bid_bet

def winner():
    manual_count = 0
    the_winner = ""
    for bidder in new_person:
        bid_amount = new_person[bidder]
        if manual_count< bid_amount:
            manual_count = bid_amount
            the_winner = bidder   #got stuck on this part of the code
    print(f"The winner is {the_winner} and they won with {manual_count} bid!") # challenge resolved!



new_person = {}
again = True
while again:
    user_name = input('What is your name?: ')
    bid_bet_original = input('How much is your bid?: ')
    new_bid(user_name, bid_bet_original)
    go_on = input("Type 'yes' if there is another person that will place a bid, type 'no' to finish: ")
    if go_on == "yes":
      print("pretend to clear console ")
    elif go_on == "no":
        again = False
        winner()


#testing code has been removed 



