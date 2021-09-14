import json
import logging

from constants import Constants


class Process:
    def __init__(self, verbose=False):
        self.log = logging.getLogger(Constants.PROCESS_LOG_NAME)
        self.log.info("Starting JSON Processor")
        self.verbose = verbose

        self.filename = ""
        self.json_string = ""
        self.filters = ""
        self.separator = ""
        self.json = None

    def set_file(self, with_filename):
        self.log.debug(f"[Selected file: {with_filename}]")
        self.filename = with_filename
        return self

    def set_filters(self, with_filters):
        self.log.debug(f"[Filters found: {with_filters}]")
        self.filters = with_filters
        return self

    def set_separator(self, with_separator):
        self.separator = with_separator if with_separator else Constants.DEFAULT_SEPARATOR
        self.log.debug(f"[Separator set: {self.separator}]")
        return self

    def read(self):
        self.log.info("Opening JSON file")
        try:
            with open(self.filename, 'r') as f:
                self.log.debug(f"[Reading JSON file: {self.filename}]")
                self.json_string = f.read()
            f.close()
            self.log.info("Reading completed")
            return self
        except IOError:
            self.log.error("File not found")
            return self

    def build(self):
        try:
            if len(self.json_string):
                self.json = json.loads(self.json_string)

                if isinstance(self.json, list):
                    self.log.debug(f"[# of JSON Objects found: {len(self.json)}]")

                self.log.info("Completed JSON processing")
                return self
            self.log.error("No JSON to process")
            return self

        except json.JSONDecodeError:
            self.log.error("JSON may be malformed. PLease check JSON syntax")
            return self
