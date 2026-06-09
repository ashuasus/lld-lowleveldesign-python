from abc import ABC, abstractmethod


# Abstract Logger class - defines the chain structure
class LogProcessor(ABC):
    DEBUG = 1
    INFO = 2
    ERROR = 3
    FATAL = 4

    def __init__(self, level):
        self.level = level
        self.next_log_processor = None

    def set_next_logger(self, next_logger):
        self.next_log_processor = next_logger

    def log_message(self, level, message):
        if self.level == level:
            self.write(message)
            return

        # Pass to next handler in chain if exists
        if self.next_log_processor is not None:
            self.next_log_processor.log_message(level, message)

    @abstractmethod
    def write(self, message):
        pass
