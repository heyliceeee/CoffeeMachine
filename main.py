from CoffeeMaker import CoffeeMaker
from Menu import Menu
from MoneyMachine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

def gui():
    global is_on
    print("🤖 Welcome to the Coffee Machine!")

    while is_on:
        options = menu.get_items()
        choice =  input(f"\nWhat would you like? ({options}report/off): ").lower()

        if choice == "off":
            print("👋 Turning off. See you next time!")
            is_on = False

        elif choice == "report":
            print("\n📊 MACHINE REPORT:")
            coffee_maker.report()
            money_machine.report()

        else:
            drink = menu.find_drink(choice)
            print(f"☕ {drink.name}: {money_machine.CURRENCY}{drink.cost:.2f}")

            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

gui()