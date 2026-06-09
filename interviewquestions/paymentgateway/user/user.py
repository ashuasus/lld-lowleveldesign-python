class User:

    def __init__(self, user_id: int = 0, user_name: str = None, email: str = None):
        self.user_id = user_id
        self.user_name = user_name
        self.email = email

    def get_user_id(self) -> int:
        return self.user_id

    def set_user_id(self, user_id: int):
        self.user_id = user_id

    def get_user_name(self) -> str:
        return self.user_name

    def set_user_name(self, user_name: str):
        self.user_name = user_name

    def get_email(self) -> str:
        return self.email

    def set_email(self, email: str):
        self.email = email

    def __str__(self) -> str:
        return f"User [userId={self.user_id}, name={self.user_name}, email={self.email}]"
