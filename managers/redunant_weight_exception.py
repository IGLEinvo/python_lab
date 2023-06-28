import logging


def logged(mode):
    def decorator(exception):
        class LoggedException(exception):
            def __init__(self, message):
                super().__init__(message)
                if mode == "console":
                    logging.error(f"Exception '{type(self).__name__}': {str(self)}")
                elif mode == "file":
                    logging.basicConfig(filename="exception.txt", level=logging.ERROR)
                    logging.error(f"Exception '{type(self).__name__}': {str(self)}")

        return LoggedException

    return decorator
