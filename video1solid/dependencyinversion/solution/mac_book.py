from ..utility.keyboard import Keyboard
from ..utility.mouse import Mouse


# Following DIP
# High-level module uses abstraction
class MacBook:
    def __init__(self, mouse, keyboard):
        self.keyboard = keyboard  # Works with any kind of keyboard and mouse
        self.mouse = mouse

    def get_mouse(self):
        return self.mouse

    def get_keyboard(self):
        return self.keyboard
