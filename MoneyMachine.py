class MoneyMachine:
    CURRENCY = "$"
    """
    currency of the money machine
    """

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    """
    coin values of the money machine
    """

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """
         prints the current profit
         :return: e.g. money: $0.0
        """
        print(f"💵 money: {self.CURRENCY}{self.profit:.2f}")

    def process_coins(self):
        """
        :return: total calculated from coins inserted
        """
        print("\n💰 Insert coins:")

        for coin, value in self.COIN_VALUES.items():
            quantity = int(input(f"How many 🪙 {coin} (${value:.2f})? : "))
            self.money_received += quantity * value

        return self.money_received

    def make_payment(self, cost):
        """
        :param cost: (float) the cost of the drink
        :return: true when payment is accepted, or false if insufficient
        """
        self.process_coins()

        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"💵 Here is your change: {self.CURRENCY}{change:.2f}")

            self.profit += cost
            self.money_received = 0
            return True

        else:
            print("❌ Not enough money. Refunding 💸")
            self.money_received = 0
            return False