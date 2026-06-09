class UserDO:
    def __init__(self, id=0, name=None, mail=None):
        self.id = id
        self.name = name
        self.mail = mail

    def __str__(self):
        return f"UserDO [uId={self.id}, name={self.name}, email={self.mail}]"
