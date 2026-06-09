from .product import Product
from .product_type import ProductType


class Item3(Product):

    def __init__(self, name: str, price: float, product_type: ProductType):
        super().__init__(name, price, product_type)

    def get_price(self) -> float:
        return self.original_price
