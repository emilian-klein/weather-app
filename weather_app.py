import requests
import json
import folium
import webbrowser
import os
import tkinter as tk
from tkinter import messagebox
from event_handler import EventHandler


class WeatherApp(tk.Tk):
    """
    Application main class.
    """
    def __init__(self):
        """
        Initialize the WeatherApp Tkinter application. Sets up the window properties, font styles and main window widgets.
        """
        super().__init__()
        self.title("Weather App")
        self.iconbitmap("images/icon.ico")
        self.geometry("400x310")
        self.resizable(False, False)
        self.font_style = ("Bahnschrift", "11", "normal")
        self.configuration = None
        self.event_handler = EventHandler(self)

        self.location_label = tk.Label(self, text="Location: ", font=self.font_style, bg="#3195DC")
        self.location_label.pack(fill="x")

        self.longitude_label = tk.Label(self, text="Longitude: ", font=self.font_style)
        self.longitude_label.pack()

        self.latitude_label = tk.Label(self, text="Latitude: ", font=self.font_style)
        self.latitude_label.pack()

        self.temperature_label = tk.Label(self, text="Temperature: ", font=self.font_style)
        self.temperature_label.pack()

        self.pressure_label = tk.Label(self, text="Pressure: ", font=self.font_style)
        self.pressure_label.pack()

        self.humidity_label = tk.Label(self, text="Humidity: ", font=self.font_style)
        self.humidity_label.pack()

        self.location_entry_sv = tk.StringVar()
        self.location_entry_sv.set("Search city...")
        self.location_entry = tk.Entry(self, textvariable=self.location_entry_sv, font=self.font_style, width=25)
        self.location_entry.pack(pady=(10, 0))
        self.location_entry.bind("<Button-1>", self.event_handler.clear_location_entry)

        self.check_weather_button = tk.Button(self, text="Check weather", command=self.event_handler.check_weather, font=self.font_style, relief="groove",
                                              bg="#787878", width=25, cursor="x_cursor", state="disabled")
        self.check_weather_button.pack(pady=(10, 0))

        self.show_on_map_button = tk.Button(self, text="See location on the map", command=self.event_handler.show_on_map, font=self.font_style,
                                            relief="groove", bg="#787878", width=25, cursor="x_cursor", state="disabled")
        self.show_on_map_button.pack(pady=(10, 0))

        self.settings_button = tk.Button(self, text="Settings", command=self.event_handler.open_settings, font=self.font_style,
                                         relief="groove", bg="#3195DC", width=25, cursor="hand2")
        self.settings_button.pack(pady=(10, 0))


if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
