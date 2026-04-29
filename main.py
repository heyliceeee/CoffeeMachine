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

currentWater = resources["water"]
currentMilk = resources["milk"]
currentCoffee = resources["coffee"]
currentMoney = resources["money"]

# function that print a report that shows the current resource values
def report():
    print(f"water: {currentWater}ml")
    print(f"milk: {currentMilk}ml")
    print(f"coffee: {currentCoffee}g")
    print(f"money: ${currentMoney}")


# function that calculate the monetary value of the coins inserted
def process_coins():
    print("insert coins: ")
    print("quarter ($0.25): ")
    quarter = float(input())

    print("dimes ($0.10): ")
    dimes = float(input())

    print("nickles ($0.05): ")
    nickles = float(input())

    print("pennies ($0.01): ")
    pennies = float(input())

    return float((0.25 * quarter) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies))


# function that check if transaction was successful
def check_transaction_successful(money_user_put_machine, cost):
    if money_user_put_machine > cost: # if user inserted enough money
        change = money_user_put_machine - cost # check change need return

        global currentMoney
        currentMoney = currentMoney + cost # insert the cost in machine

        print(f"Here is ${change:.2f} dollars in change.")
        return True

    if money_user_put_machine < cost:  # if user no inserted enough money
        print("Sorry thats not enough money. Money refunded.")
        return False

    print("Sorry thats not enough money. Money refunded.")
    return False


# function that check if have resources sufficient
def check_resources(drink):
    global currentWater
    global currentMilk
    global currentCoffee


    if drink == "espresso":

        if currentWater < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry, you don't have enough water")

        if currentCoffee < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry, you don't have enough coffee")

        if currentWater >= MENU["espresso"]["ingredients"]["water"] and currentCoffee >= MENU["espresso"]["ingredients"]["coffee"]:
            cost = MENU["espresso"]["cost"]
            print(f"The espresso is ${cost}")

            money_user_put_machine = process_coins()
            transaction = check_transaction_successful(money_user_put_machine, cost)

            if transaction is True:
                # update resources
                currentWater = currentWater - MENU["espresso"]["ingredients"]["water"]
                currentCoffee = currentCoffee - MENU["espresso"]["ingredients"]["coffee"]

                print("Here is your espresso. Enjoy!")

                report()  # show


    elif drink == "latte":
        if currentWater < MENU["latte"]["ingredients"]["water"]:
            print("Sorry, you don't have enough water")

        if currentMilk < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry, you don't have enough milk")

        if currentCoffee < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry, you don't have enough coffee")

        if currentWater >= MENU["latte"]["ingredients"]["water"] and currentMilk >= MENU["latte"]["ingredients"]["milk"] and currentCoffee >= MENU["latte"]["ingredients"]["coffee"]:
            cost = MENU["latte"]["cost"]
            print(f"The latte is ${cost}")

            money_user_put_machine = process_coins()
            transaction = check_transaction_successful(money_user_put_machine, cost)

            if transaction is True:
                # update resources
                currentWater = currentWater - MENU["latte"]["ingredients"]["water"]
                currentCoffee = currentCoffee - MENU["latte"]["ingredients"]["coffee"]
                currentMilk = currentMilk - MENU["latte"]["ingredients"]["milk"]

                print("Here is your latte. Enjoy!")

                report()  # show


    elif drink == "cappuccino":
        if currentWater < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry, you don't have enough water")

        if currentMilk < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry, you don't have enough milk")

        if currentCoffee < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry, you don't have enough coffee")

        if currentWater >= MENU["cappuccino"]["ingredients"]["water"] and currentMilk >= MENU["cappuccino"]["ingredients"]["milk"] and currentCoffee >= MENU["cappuccino"]["ingredients"]["coffee"]:
            cost = MENU["cappuccino"]["cost"]
            print(f"The cappuccino is ${cost}")

            money_user_put_machine = process_coins()
            transaction = check_transaction_successful(money_user_put_machine, cost)

            if transaction is True:
                # update resources
                currentWater = currentWater - MENU["latte"]["ingredients"]["water"]
                currentCoffee = currentCoffee - MENU["latte"]["ingredients"]["coffee"]
                currentMilk = currentMilk - MENU["latte"]["ingredients"]["milk"]

                print("Here is your cappuccino. Enjoy!")

                report()  # show


# coffee machine menu
print("welcome to coffee machine! what would you like? (espresso/latte/cappuccino):")
choice = input()

if choice == "espresso" or choice == "latte" or choice == "cappuccino":
    check_resources(choice)

if choice == "report":
    report()

if choice == "off":
    sys.exit()

if choice != "espresso" and choice != "latte" and choice != "cappuccino" and choice != "report" and choice != "off":
    print("sorry, I don't understand that. i gonna turn off coffee machine.")
    sys.exit()

while choice != "off":
    print("welcome to coffee machine! what would you like? (espresso/latte/cappuccino):")
    choice = input()

    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        check_resources(choice)

    if choice == "report":
        report()

    if choice == "off":
        sys.exit()

    if choice != "espresso" and choice  != "latte" and choice  != "cappuccino" and choice  != "report" and choice  != "off":
        print("sorry, I don't understand that. i gonna turn off coffee machine.")
        sys.exit()