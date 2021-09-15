from constants import Constants
import logging


class Filter:
    def __init__(self, separator=None, filters=None):
        self.separator = separator if separator else Constants.DEFAULT_SEPARATOR
        self.filters = filters if not filters else filters.split(self.separator)
        self.log = logging.getLogger(Constants.FILTER_LOG_NAME)
        self.log.info("Filtering JSON")
        self.log.debug(f"[Separator found: {self.separator}]")
        self.log.debug(f"[Filters found: {self.filters}]")

    def filter(self, json=None):
        in_scope_json = json

        if isinstance(in_scope_json, list):
            self.log.debug(f"[Processing JSON List: {in_scope_json}]")
            in_scope_json_list = []
            for array_object in in_scope_json:
                self.log.debug(f"[Viewing JSON List Object: {array_object}]")
                new_object = self.filter(json=array_object)
                if new_object:
                    in_scope_json_list.append(new_object)
            return in_scope_json_list if len(in_scope_json_list) else None

        elif isinstance(in_scope_json, dict):
            self.log.debug(f"[Processing JSON Object: {in_scope_json}]")
            in_scope_json_list = {}
            for json_property in in_scope_json:
                self.log.debug(f"[Viewing JSON Object property: {json_property}]")
                if self.filters and json_property in self.filters:
                    if isinstance(in_scope_json[json_property], dict):
                        json_obj = self.filter(json=in_scope_json[json_property])
                        in_scope_json_list[json_property] = json_obj
                    elif isinstance(in_scope_json[json_property], list):
                        json_list = self.filter(json=in_scope_json[json_property])
                        in_scope_json_list[json_property] = json_list
                    else:
                        in_scope_json_list[json_property] = in_scope_json[json_property]
                elif not self.filters:
                    in_scope_json_list[json_property] = in_scope_json[json_property]
            return in_scope_json_list if len(in_scope_json_list) else None
