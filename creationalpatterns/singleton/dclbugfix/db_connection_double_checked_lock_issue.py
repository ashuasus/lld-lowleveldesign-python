import threading


class DBConnectionDoubleCheckedLockIssue:
    _connection_obj = None
    _lock = threading.Lock()

    def __init__(self, port_number):
        self.port_number = port_number

    @classmethod
    def get_connection_obj(cls):
        if cls._connection_obj is None:
            with cls._lock:
                if cls._connection_obj is None:
                    cls._connection_obj = cls(5567)
        return cls._connection_obj

    def display_message(self):
        print(f"Singleton - Double Checked Locking - Issue - {self}")
