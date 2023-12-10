import logging
from colorlog import ColoredFormatter
from datetime import datetime


def setup_logger(name: str) -> logging.Logger:
    """
    Sets up a colored _logger for the application.

    Args:
        name (str): Name of the _logger.

    Returns:
        logging.Logger: Configured _logger with colored output.
    """

    # Create a _logger
    _logger = logging.getLogger(name)
    _logger.setLevel(logging.DEBUG)  # Set to your desired level

    # Create a console handler
    ch = logging.StreamHandler()
    fh = logging.FileHandler(
        "{}-{}x.log".format(name, datetime.now().strftime("%Y%m%d-%H%M%S")),
        "/logs.log",
    )
    ch.setLevel(logging.DEBUG)  # Set to your desired level

    # Create a formatter with color and bold text
    formatter = ColoredFormatter(
        "%(log_color)s%(levelname)-8s%(reset)s %(bold_white)s%(name)s%(reset)s: %(message)s",
        log_colors={
            "DEBUG": "bold_cyan",
            "INFO": "bold_green",
            "WARNING": "bold_yellow",
            "ERROR": "bold_red",
            "CRITICAL": "bold_purple",
        },
    )

    # Add formatter to the console handler
    ch.setFormatter(formatter)

    # Add console handler to the _logger
    _logger.addHandler(ch)
    _logger.addHandler(fh)

    return _logger


# Example usage
if __name__ == "__main__":
    _logger = setup_logger("DeepFieldLogger")
    _logger.debug("This is a debug message")
    _logger.info("This is an info message")
    _logger.warning("This is a warning message")
    _logger.error("This is an error message")
    _logger.critical("This is a critical message")
