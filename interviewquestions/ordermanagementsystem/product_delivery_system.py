from .user import User
from .user_controller import UserController
from .warehouse import Warehouse
from .warehouse_controller import WarehouseController
from .warehouse_selection_strategy import WarehouseSelectionStrategy
from .order import Order
from .order_controller import OrderController
from .inventory import Inventory
from .product_category import ProductCategory
from .cart import Cart


class ProductDeliverySystem:

    def __init__(self, user_list: list, warehouse_list: list):
        self.user_controller = UserController(user_list)
        self.warehouse_controller = WarehouseController(warehouse_list, None)
        self.order_controller = OrderController()

    def get_user(self, user_id: int) -> User:
        return self.user_controller.get_user(user_id)

    def get_warehouse(self, warehouse_selection_strategy: WarehouseSelectionStrategy) -> Warehouse:
        return self.warehouse_controller.select_warehouse(warehouse_selection_strategy)

    def get_inventory(self, warehouse: Warehouse) -> Inventory:
        return warehouse.inventory

    def add_product_to_cart(self, user: User, product_category: ProductCategory, count: int):
        user.get_user_cart().add_item(product_category.product_category_id, count)

    def place_order(self, user: User, warehouse: Warehouse) -> Order:
        return self.order_controller.create_new_order(user, warehouse)

    def checkout(self, order: Order):
        order.checkout()
