from .configuration_memento import ConfigurationMemento


# Originator class - creates and restores from mementos
class ApplicationConfiguration:
    def __init__(self, theme, font_size, notifications_enabled, language):
        self._theme = theme
        self._font_size = font_size
        self._notifications_enabled = notifications_enabled
        self._language = language

    # Create a memento with current state
    def save(self):
        print("[+] Saving configuration state...")
        return ConfigurationMemento(self._theme, self._font_size, self._notifications_enabled, self._language)

    # Restore state from memento
    def restore(self, memento):
        self._theme = memento.get_theme()
        self._font_size = memento.get_font_size()
        self._notifications_enabled = memento.is_notifications_enabled()
        self._language = memento.get_language()
        print("[+] Restored Previous Configuration State")

    # Setters to modify state
    def set_theme(self, theme):
        self._theme = theme

    def set_font_size(self, font_size):
        self._font_size = font_size

    def set_notifications_enabled(self, enabled):
        self._notifications_enabled = enabled

    def set_language(self, language):
        self._language = language

    def __str__(self):
        return "Configuration[Theme={}, Font Size={}, Notifications={}, Language={}]".format(
            self._theme, self._font_size, self._notifications_enabled, self._language)
