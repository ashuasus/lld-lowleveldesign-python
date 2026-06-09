from .observable.iphone_product_observable import IphoneProductObservable
from .observer.email_notification_observer import EmailNotificationObserver
from .observer.push_notification_observer import PushNotificationObserver


def main():
    print("-----------------------------------------------------------------------------")
    print("###### E-commerce Store - Stock Availability Notification Feature Demo ######")

    # Create an iPhone product - stock available = 10 units
    iphone_product = IphoneProductObservable("ip15", "iphone 15", 1250, 10)

    # Create observers
    john_push = PushNotificationObserver("John123", "JohnDeviceP1")
    katy_push = PushNotificationObserver("Katy678", "KatyDeviceP2")
    jane_email = EmailNotificationObserver("Jane783", "jane783@gmail.com")
    george_email = EmailNotificationObserver("George993", "george993@gmail.com")

    # Black Friday Sale - Purchase all 10 units
    iphone_product.purchase(10)

    # Stock unavailability leads to users subscribing for notifications
    success = iphone_product.purchase(1)  # Failed purchase
    if not success:
        # Register observers - John, Katy, Jane, George subscribe to notifications upon stock availability
        iphone_product.add_stock_observer(john_push)
        iphone_product.add_stock_observer(katy_push)
        iphone_product.add_stock_observer(jane_email)
        iphone_product.add_stock_observer(george_email)

    # Restock 20 units of iPhone 15
    iphone_product.restock(20)  # All 4 observers are notified

    # Users purchase upon receiving notifications
    iphone_product.purchase(1)  # John purchases 1 unit
    iphone_product.purchase(1)  # Katy purchases 1 unit

    # John & Katy unsubscribe from notifications
    iphone_product.remove_stock_observer(john_push)
    iphone_product.remove_stock_observer(katy_push)

    # NYE Sale - All 18 units sold
    iphone_product.purchase(18)
    iphone_product.restock(5)  # Only Jane & George are notified

    iphone_product.purchase(1)  # Jane purchases 1 unit
    iphone_product.purchase(1)  # George purchases 1 unit

    # Jane & George unsubscribe from notifications
    iphone_product.remove_stock_observer(jane_email)
    iphone_product.remove_stock_observer(george_email)


if __name__ == "__main__":
    main()
