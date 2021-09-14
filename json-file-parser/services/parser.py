import argparse


class Parser:
    def __init__(self, description):
        self.parser = argparse.ArgumentParser(description=description)
        self.parser.add_argument("filename", metavar="file", help="JSON file to parse and process")
        self.parser.add_argument("-f", "--filter", dest="filter", help="""Display only desired JSON keys, by listing 
        keys separated by : (default) or the explicitly defined separator (--separator)""")
        self.parser.add_argument("--separator", dest="separator", help="Specify a separator for filters")
        self.parser.add_argument("-v", dest="verbose", action="store_true", default=False, help="Display logging")

    def parse(self):
        options = self.parser.parse_args()
        return options
