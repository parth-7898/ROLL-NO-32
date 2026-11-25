import logging

logger = logging.getLogger("AppLogger")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("app.log", mode="w")

console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)

console_format = logging.Formatter("%(levelname)s - %(message)s")
file_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("This is a DEBUG message")
logger.info("This is an INFO message")
logger.warning("This is a WARNING message")
logger.error("This is an ERROR message")
logger.critical("This is a CRITICAL message")

try:
    result = 10 / 0

except ZeroDivisionError:
    logger.exception("Division failed")
