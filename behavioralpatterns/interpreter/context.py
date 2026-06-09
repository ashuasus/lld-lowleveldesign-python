# Context class
class Context:
    def __init__(self):
        self._variables = {}

    def set_variable(self, name, value):
        self._variables[name] = value

    def get_variable(self, name):
        return self._variables.get(name, 0)

    def __str__(self):
        return str(self._variables)
