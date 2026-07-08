from .product import Product
from .product_category import ProductCategory


class Inventory:

    def __init__(self):
        self.product_category_list = []

    def add_category(self, category_id: int, name: str, price: float):
        product_category = ProductCategory(category_id, name, price)
        self.product_category_list.append(product_category)

    def add_product(self, product: Product, product_category_id: int):
        category = self._get_category_by_id(product_category_id)
        if category:
            category.add_product(product)

    def remove_items(self, product_category_and_count_map: dict):
        for category_id, count in product_category_and_count_map.items():
            category = self._get_category_by_id(category_id)
            if category:
                category.remove_product(count)

    def _get_category_by_id(self, product_category_id: int) -> ProductCategory:
        for category in self.product_category_list:
            if category.product_category_id == product_category_id:
                return category
        return None
