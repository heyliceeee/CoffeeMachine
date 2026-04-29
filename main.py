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
    "money": 0.0
}

# function that print a report that shows the current resource values
def report():
    print("\n📊 MACHINE REPORT:")
    for item, amount in resources.items():
        unit = "ml" if item in ["water", "milk"] else "g" if item == "coffee" else ""
        emoji = "💧" if item == "water" else "🥛" if item == "milk" else "☕" if item == "coffee" else "💵"
        print(f"{emoji} {item}: {amount}{unit}")
    print()


# function that calculate the monetary value of the coins inserted
def process_coins():
    print("\n💰 Insert coins:")
    quarter = float(input("🪙 quarters ($0.25): "))
    dimes = float(input("🪙 dimes ($0.10): "))
    nickles = float(input("🪙 nickles ($0.05): "))
    pennies = float(input("🪙 pennies ($0.01): "))

    return (0.25 * quarter) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)


# function that check if machine has enough resources
def has_resources(drink):
    ingredients = MENU[drink]["ingredients"]

    for item, required in ingredients.items():
        if resources[item] < required:
            print(f"❌ Sorry, not enough {item}.")
            return False

    return True


# function that return true if transaction ok, otherwise false
def process_transaction(money_inserted, cost):
    if money_inserted < cost:
        print("❌ Not enough money. Refunding 💸")
        return False

    change = money_inserted - cost
    if change > 0:
        print(f"💵 Here is your change: ${change:.2f}")

    resources["money"] += cost
    return True


# function that deduct ingredients and serve drink
def make_drink(drink):
    ingredients = MENU[drink]["ingredients"]

    for item, amount in ingredients.items():
        resources[item] -= amount

    print(f"☕ Here is your {drink}. Enjoy! 😄")


def coffee_machine():
    print("🤖 Welcome to the Coffee Machine!")

    while True:
        choice = input("\nWhat would you like? (espresso/latte/cappuccino/report/off): ").lower()

        if choice == "off":
            print("👋 Turning off. See you next time!")
            sys.exit()

        elif choice == "report":
            report()

        elif choice in MENU:
            if not has_resources(choice):
                continue

            cost = MENU[choice]["cost"]
            print(f"💲 The {choice} costs ${cost:.2f}")

            money = process_coins()
            if process_transaction(money, cost):
                make_drink(choice)

        else:
            print("❌ Invalid option. Turning off.")
            sys.exit()

coffee_machine()