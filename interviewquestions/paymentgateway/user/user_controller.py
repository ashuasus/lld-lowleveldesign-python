from .user_do import UserDO
from .user_service import UserService


class UserController:

    def __init__(self):
        self.user_service = UserService()

    def add_user(self, user_do_obj: UserDO) -> UserDO:
        return self.user_service.add_user(user_do_obj)

    def get_user(self, user_id: int) -> UserDO:
        return self.user_service.get_user(user_id)
