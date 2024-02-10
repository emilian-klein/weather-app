import json
from tkinter import messagebox

from event_handlers.event_handler import EventHandler


class SettingsWindowEventHandler(EventHandler):
    """Class responsible for handling events which happens in settings window."""

    def save_settings(self):
        """Updates settings with data provided by user."""
        self.get_configuration()
        new_api_key = self.get_sv_value(self.window.api_key_sv)
        new_units = self.get_sv_value(self.window.units_sv)
        new_default_location = self.get_sv_value(self.window.default_location_sv)
        self.configuration["api_key"] = new_api_key
        self.configuration["units"] = new_units
        self.configuration["default_location"] = new_default_location
        self.update_configuration()
        messagebox.showinfo("Information", "Settings saved!")

    def update_configuration(self):
        """Saves current configuration to file."""
        with open("configuration.json", "w") as file:
            json.dump(self.configuration, file, indent=4)

    def close_settings(self):
        """Closes window."""
        self.window.destroy()
