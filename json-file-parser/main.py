import logging

from constants import Constants
from services.parser import Parser
from services.process import Process
from services.logger import setup as logger

options = Parser(description="Parse JSON files with filtering options").parse()

filename = options.filename
filters = options.filter
separator = options.separator
verbose = options.verbose

logger(verbose)

json = Process()\
    .set_file(with_filename=filename)\
    .set_filters(with_filters=filters)\
    .set_separator(with_separator=separator)\
    .read()\
    .build()

