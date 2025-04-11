# reason outside jupyter notebook

import logging

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(filename='myapp1.log',
                        level=logging.DEBUG,
                        format="[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")

    logger.info('Started')
    logger.info('working')
    logger.info('Finished')


if __name__ == '__main__':
    main()
