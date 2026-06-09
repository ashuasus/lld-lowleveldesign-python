from .log_processor import LogProcessor


# Concrete handler for FATAL level
class FatalLogProcessor(LogProcessor):
    def __init__(self, level):
        super().__init__(level)

    def write(self, message):
        print("FATAL: " + message)
