class User:
    def __init__(self, user_id, user_name, driving_license_no):
        self.user_id = user_id
        self.user_name = user_name
        self.driving_license_no = driving_license_no

    def get_user_id(self):
        return self.user_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_user_name(self):
        return self.user_name

    def set_user_name(self, user_name):
        self.user_name = user_name

    def get_driving_license_no(self):
        return self.driving_license_no

    def set_driving_license_no(self, driving_license_no):
        self.driving_license_no = driving_license_no
