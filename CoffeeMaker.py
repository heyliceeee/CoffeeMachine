class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def report(self):
        """
        Prints a report of all resources.
        :return: e.g. Water: 300ml | Milk: 200ml | Coffee: 100g
        """
        for item, amount in self.resources.items():
            unit = "ml" if item in ["water", "milk"] else \
                "g" if item == "coffee" else \
                    ""

            emoji = "💧" if item == "water" else \
                "🥛" if item == "milk" else \
                    "☕" if item == "coffee" else \
                        ""

            print(f"{emoji} {item}: {amount}{unit}")


    def is_resource_sufficient(self, drink):
        """
        Prints a message if ingredients are insufficient.
        :param drink: (MenuItem) the MenuItem object to make
        :return: true when the drink order can be made, false if ingredients are insufficient.
        """
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"❌ Sorry, not enough {item}.")
                return False

        return can_make


    def make_coffee(self, order):
        """
        Deducts the required ingredients from the resources.
        :param order: (MenuItem) the MenuItem object to make
        """
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]

        print(f"☕ Here is your {order.name}. Enjoy! 😄")