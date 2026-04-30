class MenuItem:
    """
    Models each menu item.
    """
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """
    Models the Menu with drinks.
    """
    def __init__(self):
        self.menu = [
            MenuItem("espresso", 50, 0, 18, 1.5),
            MenuItem("latte", 200, 150, 24, 2.5),
            MenuItem("cappuccino", 250, 100, 24, 3)
        ]

    def get_items(self):
        """
        :return: all the names of the available menu items as a concatenated string | e.g. latte/espresso/cappuccino
        """
        options = ""
        for item in self.menu:
            options += f"{item.name}/"

        return options


    def find_drink(self, order_name):
        """
        Searches the menu for a particular drink by name.
        :param order_name: (str) the name of the drinks order.
        :return: MenuItem object if it exists, otherwise None
        """
        for item in self.menu:
            if item.name == order_name:
                return item
        print("❌ Invalid option. Turning off.")