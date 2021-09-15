import logging

from services.filter import Filter
from services.parser import Parser
from services.process import Process
from services.logger import setup as logger

options = Parser(description="Parse JSON files with filtering options").parse()

filename = options.filename
filters = options.filter
separator = options.separator
verbose = options.verbose

logger(verbose)

unfiltered_json = Process()\
    .set_file(with_filename=filename)\
    .read()\
    .build()\
    .get()

filtered_json = Filter(separator=separator, filters=filters)\
    .filter(unfiltered_json)





