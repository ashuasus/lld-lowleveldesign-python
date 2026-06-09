from ..utility.wired_keyboard import WiredKeyboard
from ..utility.wired_mouse import WiredMouse


# VIOLATION OF DIP
# High-level module directly depending on low-level module
class MacBook:
    def __init__(self, wired_keyboard, wired_mouse):
        self.keyboard = wired_keyboard  # Tight coupling
        self.mouse = wired_mouse  # Tight coupling

    def get_mouse(self):
        return self.mouse

    def get_keyboard(self):
        return self.keyboard
