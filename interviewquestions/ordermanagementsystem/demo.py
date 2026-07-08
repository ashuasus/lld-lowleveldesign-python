from .product import Product
from .inventory import Inventory
from .warehouse import Warehouse
from .address import Address
from .user import User
from .nearest_warehouse_selection_strategy import NearestWarehouseSelectionStrategy
from .product_delivery_system import ProductDeliverySystem


def add_warehouse_and_inventory() -> Warehouse:
    inventory = Inventory()
    inventory.add_category(1, "Peppsii Large Cold Drink", 100)
    inventory.add_category(4, "Doovee Small Soap", 50)

    product1 = Product(1, "Peepsii")
    product2 = Product(2, "Peepsii")
    product3 = Product(3, "Doovee")

    inventory.add_product(product1, 1)
    inventory.add_product(product2, 1)
    inventory.add_product(product3, 4)

    return Warehouse(inventory=inventory)


def create_user() -> User:
    address = Address(230011, "Bengaluru", "Karnataka")
    return User(user_id=1, user_name="Abhinav", address=address)


def run_delivery_flow(product_delivery_system: ProductDeliverySystem, user_id: int):
    # 1. get user
    user = product_delivery_system.get_user(user_id)

    # 2. get nearest warehouse
    warehouse = product_delivery_system.get_warehouse(NearestWarehouseSelectionStrategy())

    # 3. browse inventory
    inventory = product_delivery_system.get_inventory(warehouse)

    product_category_to_order = None
    for category in inventory.product_category_list:
        if category.category_name == "Peppsii Large Cold Drink":
            product_category_to_order = category

    # 4. add to cart
    product_delivery_system.add_product_to_cart(user, product_category_to_order, 2)
    print(f"Cart: {user.get_user_cart().get_cart_items()}")

    # 5. place order
    order = product_delivery_system.place_order(user, warehouse)

    # 6. checkout
    product_delivery_system.checkout(order)
    print(f"Order status: {order.order_status.value}")
    print(f"Cart after checkout: {user.get_user_cart().get_cart_items()}")


def main():
    print("\n###### LLD - Order Management System Demo ######\n")

    warehouse_list = [add_warehouse_and_inventory()]
    user_list = [create_user()]

    product_delivery_system = ProductDeliverySystem(user_list, warehouse_list)
    run_delivery_flow(product_delivery_system, user_id=1)


if __name__ == "__main__":
    main()
