from .user import User


class UserController:

    def __init__(self, user_list: list):
        self.user_list = user_list

    def add_user(self, user: User):
        self.user_list.append(user)

    def remove_user(self, user: User):
        self.user_list.remove(user)

    def get_user(self, user_id: int) -> User:
        for user in self.user_list:
            if user.user_id == user_id:
                return user
        return None
