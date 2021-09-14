import argparse


class Parser:
    def __init__(self, description):
        self.parser = argparse.ArgumentParser(description=description)
        self.parser.add_argument("filename", metavar="file", help="JSON file to parse and process")
        self.parser.add_argument("-v", dest="verbose", action="store_true", default=False, help="Display logging")

    def parse(self):
        self.log.info("Parsing CLI arguments")
        options = self.parser.parse_args()
        return options
