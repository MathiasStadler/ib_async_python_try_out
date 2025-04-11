import logging
from pathlib import Path

# create log file name
log_file_name=Path(__file__).stem + ".log"

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename=log_file_name,
                        level=logging.DEBUG,
                        format="[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")

    logger.info('Started')
    logger.debug('working')
    logger.info('Finished')
