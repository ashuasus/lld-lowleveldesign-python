import threading


class DBConnectionThreadSafe:
    _instance = None
    _lock = threading.Lock()

    @classmethod
    def get_instance(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls.__new__(cls)
        return cls._instance

    def display_message(self):
        print(f"Thread Safe Singleton - {self}")
