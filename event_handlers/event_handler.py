import json


class EventHandler:
    """Base class for event handling in all application windows."""

    def __init__(self, window):
        """Sets up window context, so it establishes where event handler should operate."""
        self.window = window
        self.configuration = None

    def get_configuration(self):
        """Loads configuration to variable."""
        with open("configuration.json") as file:
            self.configuration = json.load(file)

    def get_value_from_configuration(self, key):
        """Returns specified value from configuration file."""
        self.get_configuration()

        return self.configuration.get(key)

    def get_sv_value(self, sv):
        """Returns what is currently stored in specified StringVar variable."""
        return sv.get()

    def get_mapping_for_current_units(self):
        """Returns mapping of currently selected units type."""
        current_units = self.get_value_from_configuration("units")
        mapping = self.get_value_from_configuration("units_mapping")[current_units]

        return mapping
