import os

class PriceException(Exception):
    pass

class Discount:
    def __init__(self, number_of_items, price):
        self.number_of_items = number_of_items
        self.price = price

class Checkout:
    def __init__(self):
        self.prices = {}
        self.quantities = {}
        self.discounts = {}

    def add_item(self, name):
        if name not in self.prices:
            raise PriceException("Price has not yet been added for this item!")
        if name in self.quantities:
            self.quantities[name] += 1
        else: 
            self.quantities[name] = 1

    def add_item_price(self, name, price):
        self.prices[name] = price

    def add_discount(self, name, number_of_items, price):
        self.discounts[name] = Discount(number_of_items, price)

    def apply_discounts(self):
        for discounted_item in self.discounts:
            number_of_items = self.discounts[discounted_item].number_of_items
            price = self.discounts[discounted_item].price
            while self.quantities[discounted_item] >= number_of_items:
                self.quantities[discounted_item] -= number_of_items
                if "discounted "+ discounted_item in self.quantities.keys():
                    self.quantities["discounted "+ discounted_item] += 1
                else:
                    self.quantities["discounted "+ discounted_item] = 1
                    self.prices["discounted " + discounted_item] = price

    def read_prices_from_file(self, filename):
        if not os.path.exists(filename):
            raise Exception("bad file path")
        with open(filename) as inFile:
            for line in inFile:
                tokens = line.split()
                self.add_item_price(tokens[0], int(tokens[1]))

    def subtotal(self):
        self.apply_discounts()
        item_totals = [self.quantities[item]*self.prices[item] for item in self.quantities]
        return sum(item_totals)
