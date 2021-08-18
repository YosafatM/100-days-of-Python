MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0,
}


def enough_resources(flavor):
    if MENU[flavor]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        return False
    elif MENU[flavor]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
        return False
    elif MENU[flavor]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return False

    return True


def ask_for_money():
    print("How many quarters?:")
    quarters = int(input())
    print("How many dimes?:")
    dimes = int(input())
    print("How many nickels?:")
    nickels = int(input())
    print("How many pennies?:")
    pennies = int(input())

    return 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies


def make_coffee(flavor):
    resources["money"] += MENU[flavor]["cost"]
    resources["water"] -= MENU[flavor]["ingredients"]["water"]
    resources["coffee"] -= MENU[flavor]["ingredients"]["coffee"]
    resources["milk"] -= MENU[flavor]["ingredients"]["milk"]


def return_change(money):
    if money > 0:
        print("Here is $%.2f dollars in change." % money)


def make_report():
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money: $%.1f" % resources["money"])


key = ""
while key != "off":
    print("What would you like? (espresso/latte/cappuccino):")
    key = input()

    if key == "espresso" or key == "latte" or key == "cappuccino":
        if enough_resources(key):
            change = ask_for_money() - MENU[key]["cost"]

            if change >= 0:
                make_coffee(key)
                return_change(change)
                print("Here is your " + key + " ☕ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
    elif key == "report":
        make_report()
