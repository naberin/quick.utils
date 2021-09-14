import json


class Process:
    def __init__(self, verbose=False):
        self.verbose = verbose

        self.filename = ""
        self.json_string = ""
        self.json = None

    def set_file(self, with_filename):
        self.filename = with_filename
        return self

    def read(self):
        try:
            with open(self.filename, 'r') as f:
                self.json_string = f.read()
            f.close()
            return self
        except IOError:
            return self

    def build(self):
        try:
            if len(self.json_string):
                self.json = json.loads(self.json_string)
                return self.json
            return None

        except json.JSONDecodeError:
            return None
