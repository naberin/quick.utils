from constants import Constants

import logging


def setup():
    logging.basicConfig(format=Constants.LOG_FORMAT, level=Constants.LOG_LEVEL)

