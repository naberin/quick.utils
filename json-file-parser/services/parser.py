import argparse


class Parser:

    def __init__(self, description):

        self.parser = argparse.ArgumentParser(description=description)
        self.parser.add_argument("filename", metavar="file", help="JSON file to parse and process")

    def parse(self):
        options = self.parser.parse_args()
        return options
