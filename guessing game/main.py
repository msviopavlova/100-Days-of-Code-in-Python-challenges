from art import logo
import random

#start
print(logo)
correct_number = random.choice(range(1, 101)) #TODO remove after game well tested
#print(f"Correct answer is {correct_number}")

print("Welcome to the number guessing game")
print("I am thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = 0
def new_input():
    global attempts
    if difficulty == "easy":
        attempts = 10
        print("You have 10 attempts to guess the number")
    elif difficulty == "hard":
        attempts = 5
        print("You have 5 attempts to guess the number")
    else:
        print("Invalid input try again")
        new_input()

new_input()

guess = int(input("Make a guess: "))
def check(number):
    global attempts
    while attempts>1:
        if number > correct_number:
            print("Too High")
            print("Guess again")
            attempts-=1
            print(f"You have {attempts} attempts left")
            check(int(input("What is your new guess? : ")))
        elif number < correct_number:
            print("Too Low")
            print("Guess again")
            attempts-=1
            print(f"You have {attempts} attempts left")
            check(int(input("What is your new guess? : ")))
        elif number == correct_number:
            return f"You got it! The number was {correct_number}"
    if attempts == 1 and number!=correct_number:
        return f"You Lost!, the correct number was {correct_number}"



print(check(guess))



