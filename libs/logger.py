
import logging
from rich.logging import RichHandler
from filelogger import FileLogger
# Create console handler and set its level
FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")

""" # Configure logger for file output
file_logger = logging.getLogger("file_logger")
file_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/app.log")
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
file_logger.addHandler(file_handler) """


class Logger:
    """
    A simple logging class for recording messages with different severity levels.
    """

    @staticmethod
    def debug(message: str, file_logger=False):
        """
        Logs a message with the DEBUG severity level.

        Args:
            message (str): The message to be logged.
            file_logger (bool): If true logs to file.
        """
        log.debug(message)
        if (file_logger):
            FileLogger.debug(message)

    @staticmethod
    def info(message: str, file_logger=False):
        """
        Logs a message with the INFO severity level.

        Args:
            message (str): The message to be logged.
            file_logger (bool): If true logs to file.
        """
        log.info(message)
        if (file_logger):
            FileLogger.info(message)

    @staticmethod
    def warning(message: str, file_logger=False):
        """
        Logs a message with the WARNING severity level.

        Args:
            message (str): The message to be logged.
            file_logger (bool): If true logs to file.
        """
        log.warning(message)
        if (file_logger):
            FileLogger.warning(message)

    @staticmethod
    def error(message: str, file_logger=False):
        """
        Logs a message with the ERROR severity level.

        Args:
            message (str): The message to be logged.
            file_logger (bool): If true logs to file.
        """
        log.error(message)
        if (file_logger):
            FileLogger.error(message)

    @staticmethod
    def critical(message: str, file_logger=False):
        """
        Logs a message with the CRITICAL severity level.

        Args:
            message (str): The message to be logged.
            file_logger (bool): If true logs to file.
        """
        log.critical(message)
        if (file_logger):
            FileLogger.critical(message)

    @staticmethod
    def exception(message='Exception', file_logger=False):
        """
        Logs a message with the ERROR severity level, including the exception information.

        Args:
            message (str): The message to be logged.
            file_logger (bool): If true logs to file.
        """
        log.exception(message)
        if (file_logger):
            FileLogger.exception(message)


# Logger.debug('This is message', True)
try:
    print(1 / 0)
except Exception:
    Logger.exception('New message', True)
