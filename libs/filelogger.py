
import logging

# Configure logger for file output
file_log = logging.getLogger("file_log")
file_log.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/app.log")
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
file_log.addHandler(file_handler)


class FileLogger:
    """
    A simple logging class for recording messages with different severity levels.
    """

    @staticmethod
    def debug(message: str):
        """
        Logs a message with the DEBUG severity level.

        Args:
            message (str): The message to be logged.
        """
        file_log.debug(message)

    @staticmethod
    def info(message: str):
        """
        Logs a message with the INFO severity level.

        Args:
            message (str): The message to be logged.
        """
        file_log.info(message)

    @staticmethod
    def warning(message: str):
        """
        Logs a message with the WARNING severity level.

        Args:
            message (str): The message to be logged.
        """
        file_log.warning(message)

    @staticmethod
    def error(message: str):
        """
        Logs a message with the ERROR severity level.

        Args:
            message (str): The message to be logged.
        """
        file_log.error(message)

    @staticmethod
    def critical(message: str):
        """
        Logs a message with the CRITICAL severity level.

        Args:
            message (str): The message to be logged.
        """
        file_log.critical(message)

    @staticmethod
    def exception(message='Exception'):
        """
        Logs a message with the ERROR severity level, including the exception information.

        Args:
            message (str): The message to be logged.
        """
        file_log.exception(message)
        # file_log.debug("This is a debug message for file")
