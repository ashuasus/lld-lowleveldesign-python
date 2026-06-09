from .stock_availability_observable import StockAvailabilityObservable


# Concrete Observable
class IphoneProductObservable(StockAvailabilityObservable):
    def __init__(self, product_id, product_name, price, stock_quantity):
        self._product_id = product_id
        self._product_name = product_name
        self._price = price
        self._stock_quantity = stock_quantity
        self._stock_observers = []

    def add_stock_observer(self, observer):
        self._stock_observers.append(observer)
        print("[+]" + observer.get_user_id() + " subscribed for notifications on " + self._product_name)

    def remove_stock_observer(self, observer):
        self._stock_observers.remove(observer)
        print("[-]" + observer.get_user_id() + " unsubscribed for notifications on " + self._product_name)

    def notify_stock_observers(self):
        if self._stock_quantity > 0 and self._stock_observers:
            print("Notifying " + str(len(self._stock_observers)) + " subscribers... ")

            # Create a copy to avoid concurrent modification
            observers_to_notify = list(self._stock_observers)

            for observer in observers_to_notify:
                observer.update()

    # Method to restock items
    def restock(self, quantity):
        was_out_of_stock = (self._stock_quantity == 0)
        self._stock_quantity += quantity
        print("RESTOCKED: " + self._product_name + " - Added " + str(quantity) + " items " + " | " + "Current stock: " + str(self._stock_quantity))
        # Only notify if product was previously out of stock
        if was_out_of_stock and self._stock_quantity > 0:
            self.notify_stock_observers()

    # Method to purchase items
    def purchase(self, quantity):
        if self._stock_quantity >= quantity:
            self._stock_quantity -= quantity
            print("PURCHASE SUCCESS: " + str(quantity) + " units of " + self._product_name + " | " + "Remaining stock: " + str(self._stock_quantity))
            return True
        else:
            print("PURCHASE FAILED: " + self._product_name + " is out of stock! | " + "Available Quantity: " + str(self._stock_quantity))
            return False

    # Getters
    def get_product_id(self):
        return self._product_id

    def get_product_name(self):
        return self._product_name

    def get_price(self):
        return self._price

    def get_stock_quantity(self):
        return self._stock_quantity
