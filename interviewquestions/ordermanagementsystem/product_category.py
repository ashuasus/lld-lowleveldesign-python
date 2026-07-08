from .product import Product


class ProductCategory:

    def __init__(self, product_category_id: int, category_name: str, price: float):
        self.product_category_id = product_category_id
        self.category_name = category_name
        self.price = price
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, count: int):
        for _ in range(count):
            if self.products:
                self.products.pop(0)
