from constants import Constants

import logging


def setup(verbose=False):
    logging.basicConfig(format=Constants.LOG_FORMAT, level=Constants.LOG_LEVEL)

    if not verbose:
        logging.disable(logging.DEBUG)
        logging.disable(logging.CRITICAL)
        logging.disable(logging.ERROR)
        logging.disable(logging.WARNING)
        logging.disable(logging.INFO)

