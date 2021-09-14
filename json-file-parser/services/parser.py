import argparse
import logging

from constants import Constants


class Parser:

    def __init__(self, description):
        self.log = logging.getLogger(Constants.PARSER_LOG_NAME)
        self.log.info("Starting CLI")
        self.parser = argparse.ArgumentParser(description=description)
        self.parser.add_argument("filename", metavar="file", help="JSON file to parse and process")

    def parse(self):
        self.log.info("Parsing CLI arguments")
        options = self.parser.parse_args()
        return options
