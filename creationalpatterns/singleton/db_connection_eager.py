class DBConnectionEager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()

    def display_message(self):
        print(f"Eager Initialization - Singleton - {self}")


# Eagerly create the instance at module load time
DBConnectionEager._instance = DBConnectionEager()
