from .stock_notification_observer import StockNotificationObserver


# Concrete observer for push notifications
class PushNotificationObserver(StockNotificationObserver):
    def __init__(self, user_id, device_token):
        self._user_id = user_id
        self._device_token = device_token

    def update(self):
        self._send_push_notification()

    def _send_push_notification(self):
        print("!! PUSH NOTIFICATION SENT to: " + self._device_token + " - " + "Product is back in stock! Hurry Up!!")

    def get_notification_method(self):
        return "Push Notification"

    def get_user_id(self):
        return self._user_id
