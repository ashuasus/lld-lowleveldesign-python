from .log_processor import LogProcessor


# Concrete handler for INFO level
class InfoLogProcessor(LogProcessor):
    def __init__(self, level):
        super().__init__(level)

    def write(self, message):
        print("INFO: " + message)
