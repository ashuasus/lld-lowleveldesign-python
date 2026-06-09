class VehicleRentalSystem:
    def __init__(self):
        self.store_list = []
        self.user_list = []

    def get_store(self, store_id):
        for store in self.store_list:
            if store.get_store_id() == store_id:
                return store
        return None

    def get_user(self, user_id):
        return self.user_list[user_id]

    def add_store(self, store):
        self.store_list.append(store)

    def add_user(self, user):
        self.user_list.append(user)

    def remove_store(self, store_id):
        self.store_list = [s for s in self.store_list if s.get_store_id() != store_id]

    def remove_user(self, user_id):
        self.user_list.pop(user_id)
