from constants import Constants

import logging


def setup():
    logging.getLogger(Constants.LOG_NAME)
    logging.basicConfig(format=Constants.LOG_FORMAT, level=Constants.LOG_LEVEL)

