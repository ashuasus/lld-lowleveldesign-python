import random
from .user import User
from .user_do import UserDO


class UserService:

    users_list: list = []  # static: shared across all instances

    def add_user(self, user_do: UserDO) -> UserDO:
        # do some validations
        user_obj = User()
        user_obj.set_user_name(user_do.get_name())
        user_obj.set_email(user_do.get_mail())
        user_obj.set_user_id(random.randint(10, 99))
        UserService.users_list.append(user_obj)
        return self._convert_user_do_to_user(user_obj)

    def _convert_user_do_to_user(self, user_obj: User) -> UserDO:
        user_do = UserDO()
        user_do.set_name(user_obj.get_user_name())
        user_do.set_mail(user_obj.get_email())
        user_do.set_id(user_obj.get_user_id())
        return user_do

    def get_user(self, user_id: int) -> UserDO:
        for user in UserService.users_list:
            if user.get_user_id() == user_id:
                return self._convert_user_do_to_user(user)
        return None
