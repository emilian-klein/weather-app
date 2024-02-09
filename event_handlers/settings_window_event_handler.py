import json
from tkinter import messagebox

from event_handlers.event_handler import EventHandler


class SettingsWindowEventHandler(EventHandler):
    """Class responsible for handling events in which happens in settings window."""

    def set_api_key_sv(self):
        """Returns api_key value saved in configuration to paste it into entry widget."""
        self.get_configuration()
        return self.configuration.get("api_key")

    def set_units_sv(self):
        """Returns units value saved in configuration to make a selection of proper radiobutton widget."""
        self.get_configuration()
        return self.configuration.get("units")

    def save_api_key(self):
        """Updates api_key value in configuration with value fetch from enter widget."""
        new_api_key = self.get_api_key()
        new_units = self.get_units()
        self.configuration["api_key"] = new_api_key
        self.configuration["units"] = new_units
        self.update_configuration()
        messagebox.showinfo("Information", "Settings saved!")

    def get_api_key(self):
        """Reads what is currently presented in 'API Key' entry field."""
        return str(self.window.api_key_sv.get())

    def get_units(self):
        """Reads what is currently selected in 'Units' submenu."""
        return str(self.window.units_sv.get())

    def update_configuration(self):
        """Saves current configuration to file."""
        with open("configuration.json", "w") as file:
            json.dump(self.configuration, file, indent=4)

    def close_settings(self):
        """Closes window."""
        self.window.destroy()
