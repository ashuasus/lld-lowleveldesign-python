class Item:
    def __init__(self):
        self.type = None
        self.price = 0

    def get_type(self):
        return self.type

    def set_type(self, item_type):
        self.type = item_type

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price
