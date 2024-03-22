import json


class EventHandler:
    def __init__(self, window):
        self.window = window
        self.configuration = None

    def get_configuration(self):
        with open("configuration.json") as file:
            self.configuration = json.load(file)

    def get_value_from_configuration(self, key):
        self.get_configuration()

        return self.configuration.get(key)

    def get_sv_value(self, sv):
        return sv.get()

    def get_mapping_for_current_units(self):
        current_units = self.get_value_from_configuration("units")
        mapping = self.get_value_from_configuration("units_mapping")[current_units]

        return mapping
