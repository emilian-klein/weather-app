import json
from tkinter import messagebox


class SettingsWindowEventHandler:
    def __init__(self, window):
        self.window = window
        self.configuration = None

    def get_configuration(self):
        with open("configuration.json") as file:
            self.configuration = json.load(file)

    def set_api_key_sv(self):
        self.get_configuration()
        return self.configuration.get("api_key", "")

    def save_api_key(self):
        new_api_key = self.get_new_api_key()
        self.configuration["api_key"] = new_api_key
        self.update_configuration()
        messagebox.showinfo("Information", "API key saved!")
        self.close_settings()

    def get_new_api_key(self):
        return str(self.window.api_key_sv.get())

    def update_configuration(self):
        with open("configuration.json", "w") as file:
            json.dump(self.configuration, file, indent=4)

    def close_settings(self):
        self.window.destroy()
