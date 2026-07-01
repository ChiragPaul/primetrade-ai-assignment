import logging
import sys

def setup_logger(name="trading_bot", log_file="trading_bot.log", level=logging.INFO):
    """
    Sets up a logger that outputs to both a file and the console.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        # Formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # File Handler (Detailed logs)
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)  # Log debug and above to file
        file_handler.setFormatter(formatter)

        # Console Handler (Only INFO and above, for cleaner CLI output)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
