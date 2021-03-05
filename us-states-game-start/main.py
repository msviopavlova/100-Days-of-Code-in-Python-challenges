import turtle
import pandas


screen = turtle.Screen()

screen.title(f"U.S. States Game")
image = "blank_states_img.gif"

# Loading an image into the Turtle game using screen and afterwards turtle shape becomes the image
screen.addshape(image)
turtle.shape(image)

list_of_guesses = []

game_is_on = True
while len(list_of_guesses) < 50:


    answer_state = screen.textinput(title = " Guess the state", prompt = f"What's another state's name? You guessed {len(list_of_guesses)}/50")
    guess = answer_state.title()

    #Reading and working with the list states in CSV format
    data = pandas.read_csv("50_states.csv")
    list_of_states = data.state.to_list()

    if guess == "Exit":
        break
    if guess in list_of_states:

        list_of_guesses.append(guess)
        #Getting the row of the guess

        the_row_of_the_guess = data[data["state"] == guess]

        # Converting the data into a python dictionary
        guess_dict_parameters = the_row_of_the_guess.to_dict()


        # Get the name of the state without knowing the key
        current_state_key = guess_dict_parameters["state"]

        for key in current_state_key:
            actual_current_state = list(current_state_key.values())[0]


        # Getting the x and y without knowing the key name of the dictionary (this is my solution):
        x_dict = guess_dict_parameters["x"]
        for key in x_dict:
            x = list(x_dict.values())[0]


        y_dict = guess_dict_parameters["y"]
        for key in y_dict:
            y = list(y_dict.values())[0]


        print(f"whole dictionary = {guess_dict_parameters}, x= {x}, y = {y}")

        #Creating a Turtle and it writes the state onto the map in the correct location
        vio = turtle.Turtle()
        vio.penup()
        vio.hideturtle()
        vio.goto(x, y)
        vio.write(actual_current_state)

        print(list_of_guesses)




#states_to_learn.csv

