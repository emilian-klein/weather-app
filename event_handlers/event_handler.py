import json


class EventHandler:
    def __init__(self, window):
        self.window = window
        self.configuration = None

    def get_configuration(self):
        with open("configuration.json") as file:
            self.configuration = json.load(file)
