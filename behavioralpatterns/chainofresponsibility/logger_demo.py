from .log_processor import LogProcessor
from .fatal_log_processor import FatalLogProcessor
from .error_log_processor import ErrorLogProcessor
from .info_log_processor import InfoLogProcessor
from .debug_log_processor import DebugLogProcessor


# Client code
def main():
    print("###### Chain of Responsibility Design Pattern ######")

    # Get the chain of loggers
    log_processor = get_chain_of_loggers()

    print("Logging messages:")
    print("===== Logging DEBUG message =====")
    log_processor.log_message(LogProcessor.DEBUG, "This is a debug message")
    print("===== Logging INFO message =====")
    log_processor.log_message(LogProcessor.INFO, "This is an info message")
    print("===== Logging ERROR message =====")
    log_processor.log_message(LogProcessor.ERROR, "This is an error message")
    print("===== Logging FATAL message =====")
    log_processor.log_message(LogProcessor.FATAL, "This is a fatal message")


def get_chain_of_loggers():
    fatal_logger = FatalLogProcessor(LogProcessor.FATAL)
    error_logger = ErrorLogProcessor(LogProcessor.ERROR)
    info_logger = InfoLogProcessor(LogProcessor.INFO)
    debug_logger = DebugLogProcessor(LogProcessor.DEBUG)

    #  Dynamic Chaining: DEBUG -> INFO -> ERROR -> FATAL
    debug_logger.set_next_logger(info_logger)
    info_logger.set_next_logger(error_logger)
    error_logger.set_next_logger(fatal_logger)

    return debug_logger  # Return the first LogProcessor in chain


if __name__ == "__main__":
    main()
