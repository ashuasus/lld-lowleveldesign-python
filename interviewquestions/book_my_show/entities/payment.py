import uuid


class Payment:
    def __init__(self, status):
        self._payment_id = uuid.uuid4()
        self._status = status

    def get_payment_id(self):
        return self._payment_id

    def get_status(self):
        return self._status
