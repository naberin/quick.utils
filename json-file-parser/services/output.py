import pandas as pd


class Output:
    def __init__(self):
        self.keys = {}

    def flatten(self, json=None, parent_key=""):
        if isinstance(json, list):
            for i in range(0, len(json)):
                self.flatten(json[i], parent_key=parent_key)

        elif isinstance(json, dict):
            for key in json:
                pk = f"{key}" if not parent_key else f"{parent_key}.{key}"
                if isinstance(json[key], dict) or isinstance(json[key], list):

                    self.flatten(json[key], parent_key=pk)
                else:
                    object_key = pk if parent_key != "" else key
                    if object_key in self.keys:

                        self.keys[object_key].append(json[key])
                    else:

                        self.keys[object_key] = [json[key]]
        return self

    def display(self, as_file=None):
        df = pd.DataFrame(self.keys)
        if as_file:
            df.to_csv(as_file, index=False)
        else:
            df.to_csv(index=False)
            print(df)
