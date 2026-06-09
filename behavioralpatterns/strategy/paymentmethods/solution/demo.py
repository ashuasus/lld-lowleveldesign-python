from .strategy.credit_card_payment import CreditCardPayment
from .strategy.pay_pal_payment import PayPalPayment
from .strategy.upi_payment import UPIPayment
from .shopping_cart import ShoppingCart


# Client code - to simulate payment processing
def main():
    print("###### Strategy Design Pattern ######")
    print("###### Example: Payment Processor ######")

    # Create a shopping cart and set payment strategy
    cart = ShoppingCart()

    # Choosing payment behavior at runtime
    cart.set_payment_strategy(CreditCardPayment("1234-5678-9012-3456"))
    cart.checkout(100.0)
    cart.set_payment_strategy(PayPalPayment("johndoe@example.com"))
    cart.checkout(200.0)
    cart.set_payment_strategy(UPIPayment("9988776655@ybl"))
    cart.checkout(300.0)


if __name__ == "__main__":
    main()
