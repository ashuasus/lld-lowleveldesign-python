from ..product.product import Product
from ..product.product_type import ProductType
from .coupon_decorator import CouponDecorator


class TypeCouponDecorator(CouponDecorator):

    eligible_types = [ProductType.FURNITURE, ProductType.ELECTRONICS]

    def __init__(self, product: Product, percentage: int):
        super().__init__(product, percentage)

    def get_price(self) -> float:
        price = self.product.get_price()
        if self.product.get_type() in self.eligible_types:
            price_after_discount = price - (price * self.discount_percentage) / 100
            print(f"Applying specific product type coupon of {self.discount_percentage}% on {self.product.get_name()}, "
                  f"original price : {price}, price after discount : {price_after_discount}")
            return price_after_discount
        return price
