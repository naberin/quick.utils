import logging

from constants import Constants
from services.parser import Parser
from services.process import Process
from services.logger import setup as logger

logger()
options = Parser(description="Parse JSON files with filtering options").parse()

filename = options.filename

json = Process()\
    .set_file(with_filename=filename)\
    .read()\
    .build()

