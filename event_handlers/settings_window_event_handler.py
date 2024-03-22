import json
from tkinter import messagebox

from event_handlers.event_handler import EventHandler


class SettingsWindowEventHandler(EventHandler):
    def save_settings(self, event=None):
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
        with open("configuration.json", "w") as file:
            json.dump(self.configuration, file, indent=4)

    def close_settings(self):
        self.window.destroy()
