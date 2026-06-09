from .log_processor import LogProcessor


# Concrete handler for DEBUG level
class DebugLogProcessor(LogProcessor):
    def __init__(self, level):
        super().__init__(level)

    def write(self, message):
        print("DEBUG: " + message)
