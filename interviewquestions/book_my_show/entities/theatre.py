class Theatre:
    def __init__(self, name, city, screens):
        self._name = name
        self._city = city
        self._screens = screens

    def get_city(self):
        return self._city

    def get_name(self):
        return self._name

    def get_screens(self):
        return self._screens
