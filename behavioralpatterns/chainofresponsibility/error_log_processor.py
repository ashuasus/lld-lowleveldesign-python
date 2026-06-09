from .log_processor import LogProcessor


# Concrete handler for ERROR level
class ErrorLogProcessor(LogProcessor):
    def __init__(self, level):
        super().__init__(level)

    def write(self, message):
        print("ERROR: " + message)
