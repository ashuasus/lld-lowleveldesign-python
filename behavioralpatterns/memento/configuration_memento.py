# Memento class - stores the state
class ConfigurationMemento:
    def __init__(self, theme, font_size, notifications_enabled, language):
        self._theme = theme
        self._font_size = font_size
        self._notifications_enabled = notifications_enabled
        self._language = language

    # Getters for restoration
    def get_theme(self):
        return self._theme

    def get_font_size(self):
        return self._font_size

    def is_notifications_enabled(self):
        return self._notifications_enabled

    def get_language(self):
        return self._language

    def __str__(self):
        return "ConfigurationMemento[Theme={}, Font Size={}, Notifications={}, Language={}]".format(
            self._theme, self._font_size, self._notifications_enabled, self._language)
