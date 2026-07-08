from .inventory import Inventory
from .address import Address


class Warehouse:

    def __init__(self, inventory: Inventory = None, address: Address = None):
        self.inventory = inventory
        self.address = address

    def remove_item_from_inventory(self, product_category_and_count_map: dict):
        self.inventory.remove_items(product_category_and_count_map)

    def add_item_to_inventory(self, product_category_and_count_map: dict):
        pass
