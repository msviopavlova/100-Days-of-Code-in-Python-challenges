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


choice = input("What would you like? (espresso/latte/cappuccino): ")

order = MENU[choice]

order_cost = order["cost"]
print(f"Please insert coins. The price is {order_cost}")

quarters_given = int(input("How many quarters? "))
dimes_given = int(input("How many dimes? "))
nickles_given = int(input("How many nickles? "))
pennies_given = int(input("How many pennies? "))
# TODO add up all money given.

quarter = 0.25
dime = 0.10
nickle = 0.05
penny = 0.01

payment = (quarters_given * quarter)+(dimes_given * dime)+(nickles_given * nickle)+(pennies_given * penny)
print(f"You have paid: {payment}")

#TODO check is payment higher than the cost ?

if payment > order_cost:
    change = -(order_cost-payment)
    print(f"Here is you change ${change}")
else:
    print("Insufficient amount, money refunded")




