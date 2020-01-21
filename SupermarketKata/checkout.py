class Checkout:
    def __init__(self):
        self.prices = {}
        self.total = 0

    def add_item(self, name):
        self.total += self.prices[name]

    def add_item_price(self, name, price):
        self.prices[name] = price

    def subtotal(self):
        return self.total
