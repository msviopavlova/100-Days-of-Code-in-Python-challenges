from art import logo
import random

#start

correct_number = random.choice(range(1, 101)) #TODO remove after game well tested
print(f"Correct answer is {correct_number}")

print("Welcome to the number guessing game")
print("I am thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = 0

if difficulty == "easy":
    attempts = 10
    print("You have 10 attempts to guess the number")
elif difficulty == "hard":
    attempts = 5
    print("You have 5 attempts to guess the number")

guess = int(input("Make a guess: "))
def check(number):
    global attempts

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
        print(f"You got it! The number was {correct_number}")



check(guess)



