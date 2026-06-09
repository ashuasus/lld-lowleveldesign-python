from .stock_notification_observer import StockNotificationObserver


# Concrete observer for email notifications
class EmailNotificationObserver(StockNotificationObserver):
    def __init__(self, user_id, email_address):
        self._user_id = user_id
        self._email_address = email_address

    def update(self):
        self._send_email()

    def _send_email(self):
        print("!! EMAIL SENT to: " + self._email_address + " - " + "Product is back in stock! Hurry Up!!")

    def get_notification_method(self):
        return "Email"

    def get_user_id(self):
        return self._user_id
