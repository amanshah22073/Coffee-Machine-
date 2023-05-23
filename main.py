
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
cash = MoneyMachine()
Menu_card = Menu()
machine  = CoffeeMaker()

def Coffee_machine():
    system = True
    while system:
        choice = input(f"What would you like? ({Menu_card.get_items()}): ")
        if choice == "report":
            machine.report()
            cash.report()
        elif choice == "off":
            system = False
        else:
            drink = Menu_card.find_drink(choice)
            if machine.is_resource_sufficient(drink):
                if cash.make_payment(drink.cost):
                    machine.make_coffee(drink)

Coffee_machine()

