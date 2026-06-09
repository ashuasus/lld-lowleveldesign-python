from ..product.product import Product
from ..product.product_type import ProductType


class CouponDecorator(Product):

    def __init__(self, product: Product, discount_percentage: int):
        super().__init__(product.get_name(), product.get_price(), product.get_type())
        self.product = product
        self.discount_percentage = discount_percentage
