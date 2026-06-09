class DBConnectionLazy:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance

    def display_message(self):
        print(f"Lazy Initialization - Singleton - {self}")
