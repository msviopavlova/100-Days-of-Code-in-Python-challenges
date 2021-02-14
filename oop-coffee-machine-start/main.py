from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
is_on = True

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()



money_machine.report()
coffee_maker.report()


while is_on:
    option = menu.get_items()
    choice = input(f"What would you like? {option}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        print(drink)
       if coffee_maker.is_resource_sufficient(drink):
           money_machine.make_payment(drink)




