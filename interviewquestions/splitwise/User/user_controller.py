class UserController:
    def __init__(self):
        self.user_list = []

    def add_user(self, user):
        self.user_list.append(user)

    def get_user(self, user_id):
        for user in self.user_list:
            if user.get_user_id() == user_id:
                return user
        return None

    def get_all_users(self):
        return self.user_list
