from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Money_Machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

on = True

while on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        on = False
    elif choice == "report":
        coffee_maker.report()
        Money_Machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and Money_Machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



