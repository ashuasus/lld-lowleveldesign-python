from .invoice import Invoice
from .payment import Payment
from .payment_mode import PaymentMode
from .upi_payment_mode import UPIPaymentMode
from .order_status import OrderStatus


class Order:

    def __init__(self, user, warehouse):
        self.user = user
        self.warehouse = warehouse
        self.product_category_and_count_map = user.get_user_cart().get_cart_items().copy()
        self.delivery_address = user.address
        self.payment = None
        self.order_status = OrderStatus.UNDELIVERED
        self.invoice = Invoice()
        self.invoice.generate_invoice(self)

    def checkout(self):
        # 1. update inventory
        self.warehouse.remove_item_from_inventory(self.product_category_and_count_map)

        # 2. make payment
        is_payment_success = self.make_payment(UPIPaymentMode())

        # 3. empty cart on success, rollback inventory on failure
        if is_payment_success:
            self.user.get_user_cart().empty_cart()
            self.order_status = OrderStatus.DELIVERED
        else:
            self.warehouse.add_item_to_inventory(self.product_category_and_count_map)
            self.order_status = OrderStatus.CANCELLED

    def make_payment(self, payment_mode: PaymentMode) -> bool:
        self.payment = Payment(payment_mode)
        return self.payment.make_payment()
