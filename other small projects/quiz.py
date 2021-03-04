order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
#got value for "Steak"
print(order["starter"][1])

new_person = {
    "Violetta": 1500,
}

for key in  new_person:
    print(new_person[key])