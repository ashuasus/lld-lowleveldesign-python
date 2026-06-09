from .coupons.percentage_coupon_decorator import PercentageCouponDecorator
from .coupons.type_coupon_decorator import TypeCouponDecorator
from .product.product import Product


class ShoppingCart:

    def __init__(self):
        self.product_list = []

    def add_to_cart(self, product: Product):
        # Decorate the Product with applicable coupons
        product_with_eligible_discount = TypeCouponDecorator(
            PercentageCouponDecorator(product, 20), 10
        )
        self.product_list.append(product_with_eligible_discount)

    def get_total_price(self) -> float:
        total_price = 0.0

        # product_list contains decorated products
        for product in self.product_list:
            total_price += product.get_price()  # get_price() will return the price after applying the coupons

        return total_price
