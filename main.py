import sys

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

# coffee machine menu
print("welcome to coffee machine! what would you like? (espresso/latte/cappuccino):")
choice = input()

match choice:
    case "espresso":
        print("espresso")

    case "latte":
        print("latte")

    case "cappuccino":
        print("cappuccino")

    case "report":
        print("report")

    case "off":
        sys.exit()

    case _:
        print("sorry, I don't understand that. i gonna turn off coffee machine.")
        sys.exit()