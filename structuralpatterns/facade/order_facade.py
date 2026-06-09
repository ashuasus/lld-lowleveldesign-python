from .inventory_service import InventoryService
from .payment_service import PaymentService
from .shipping_service import ShippingService
from .notification_service import NotificationService


# Facade hides complexity and provides a simple unified interface
class OrderFacade:
    def __init__(self):
        self.inventory = InventoryService()
        self.payment = PaymentService()
        self.shipping = ShippingService()
        self.notification = NotificationService()

    # Simplified method for clients
    def place_order(self, product_id, payment_method):
        # The following steps are hidden from the client and need to be executed in a specific order
        print("Placing order for product: " + product_id)

        # Step 1: Check stock
        if not self.inventory.check_stock(product_id):
            print("Product out of stock!")
            return

        # Step 2: Make payment
        if not self.payment.make_payment(payment_method):
            print("Payment failed!")
            return

        # Step 3: Ship product
        self.shipping.ship_product(product_id)

        # Step 4: Send confirmation
        self.notification.send_confirmation(product_id)

        print("Order placed successfully!")
