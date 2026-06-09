from ..product.product import Product
from .coupon_decorator import CouponDecorator


class PercentageCouponDecorator(CouponDecorator):

    def __init__(self, product: Product, percentage: int):
        super().__init__(product, percentage)

    def get_price(self) -> float:
        price = self.product.get_price()
        price_after_discount = price - (price * self.discount_percentage) / 100
        print(f"Applying percentage coupon of {self.discount_percentage}% on {self.product.get_name()}, "
              f"original price : {price}, price after discount : {price_after_discount}")
        return price_after_discount
