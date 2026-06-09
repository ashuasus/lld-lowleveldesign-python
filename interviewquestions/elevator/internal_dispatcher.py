class InternalDispatcher:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @staticmethod
    def get_instance():
        return InternalDispatcher()

    def submit_internal_request(self, destination_floor, controller):
        controller.submit_request(destination_floor)
