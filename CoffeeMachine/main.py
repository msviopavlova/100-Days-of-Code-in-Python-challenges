MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#print(f"{resources} resources before ")

def get_change():
    global make_coffee
    if payment > order_cost:
        change = -(order_cost - payment)
        print(f"Here is your change ${change}")
        ingredients(resources)
    else:
        print("Insufficient amount, money refunded")
        make_coffee = False




def ingredients(resources):
    global make_coffee
    for ing in resources:
        order_ingredients = order["ingredients"]
        if resources[ing] > order_ingredients[ing]:
            leftover = resources[ing] - order_ingredients[ing]
            resources[ing] = leftover
            return resources
        elif resources[ing] < order_ingredients[ing]:
            print(f"Sorry, there isn't enough {ing} in the coffee machine")
            make_coffee = False




make_coffee = True
while make_coffee:
    choice = input("What would you like? (espresso/latte/cappuccino)  ☕  : ")

    if choice == "report":
        for ing in resources:
            print(f"{ing}: {resources[ing]}")
    elif choice == "off":
        print("Machine off 👋")
        make_coffee = False
    else:
        order = MENU[choice]
        order_cost = order["cost"]
        print(f"Please insert coins 💵. The price is {order_cost}")

        quarters_given = int(input("How many quarters? "))
        dimes_given = int(input("How many dimes? "))
        nickles_given = int(input("How many nickles? "))
        pennies_given = int(input("How many pennies? "))

        quarter = 0.25
        dime = 0.10
        nickle = 0.05
        penny = 0.01

        payment = (quarters_given * quarter)+(dimes_given * dime)+(nickles_given * nickle)+(pennies_given * penny)
        print(f"You have paid: {payment}")

        get_change()






