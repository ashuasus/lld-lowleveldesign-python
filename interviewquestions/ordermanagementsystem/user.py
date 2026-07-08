from .cart import Cart
from .address import Address


class User:

    def __init__(self, user_id: int, user_name: str, address: Address):
        self.user_id = user_id
        self.user_name = user_name
        self.address = address
        self.user_cart = Cart()
        self.order_ids = []

    def get_user_cart(self) -> Cart:
        return self.user_cart
