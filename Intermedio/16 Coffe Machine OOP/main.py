from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()

while True:
    option = input("What would you like? " + menu.get_items() + ":")

    if option == "off":
        break
    elif option == "report":
        maker.report()
        money.report()
    else:
        item = menu.find_drink(option)

        if item is None:
            pass

        if maker.is_resource_sufficient(item):
            if money.make_payment(item.cost):
                maker.make_coffee(item)
