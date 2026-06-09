from .product.item1 import Item1
from .product.item2 import Item2
from .product.item3 import Item3
from .product.item4 import Item4
from .product.product_type import ProductType
from .shopping_cart import ShoppingCart


def main():
    print("\n###### LLD - Coupon Application System Demo ######\n")

    # Create Products
    item1 = Item1("Fan", 1500, ProductType.ELECTRONICS)
    item2 = Item2("Office Chair", 6000, ProductType.FURNITURE)
    item3 = Item3("Omega3-Tabs", 600, ProductType.PHARMACY)
    item4 = Item4("Shirt", 1200, ProductType.CLOTHES)

    # Shopping Cart
    cart = ShoppingCart()
    cart.add_to_cart(item1)
    cart.add_to_cart(item2)
    cart.add_to_cart(item3)
    cart.add_to_cart(item4)

    # Calculate Total Price
    print("\n===>>> Total Price after discount: " + str(cart.get_total_price()))


if __name__ == "__main__":
    main()
