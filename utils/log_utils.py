import logging
import os


def setup_logger(name, log_file, level=logging.INFO):
    log_dir = "logging"
    os.makedirs(log_dir, exist_ok=True)  # Ensure the logging directory exists
    log_file_path = os.path.join(log_dir, log_file)

    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler = logging.FileHandler(log_file_path)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
