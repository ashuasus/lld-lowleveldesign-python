from .order import Order
from .user import User
from .warehouse import Warehouse


class OrderController:

    def __init__(self):
        self.order_list = []
        self.user_id_vs_orders = {}

    def create_new_order(self, user: User, warehouse: Warehouse) -> Order:
        order = Order(user, warehouse)
        self.order_list.append(order)

        if user.user_id in self.user_id_vs_orders:
            self.user_id_vs_orders[user.user_id].append(order)
        else:
            self.user_id_vs_orders[user.user_id] = [order]

        return order

    def remove_order(self, order: Order):
        self.order_list.remove(order)

    def get_orders_by_user_id(self, user_id: int) -> list:
        return self.user_id_vs_orders.get(user_id, [])
