import json
import os
import webbrowser
from tkinter import messagebox

import requests
import folium

from windows.settings_window import SettingsWindow


class MainWindowEventHandler:
    def __init__(self, window):
        self.window = window
        self.configuration = None

    def get_configuration(self):
        with open("configuration.json") as file:
            self.configuration = json.load(file)

    def clear_location_entry(self, event):
        """
        Clears the location entry widget when clicked.
        """
        self.window.location_entry.delete(0, "end")

    def check_weather(self):
        self.get_configuration()
        location = self.get_location()
        weather_data = self.get_weather_data(location)
        self.update_weather_labels(weather_data)

    def get_location(self):
        return str(self.window.location_entry.get())

    def get_weather_data(self, location):
        """
        Retrieve specific weather data for the entered location from the OpenWeather API.
        """
        response = self.make_api_request(location)
        data = response.json()
        if response.status_code == 200:
            weather_data = {
                "temperature": str(data["main"]["temp"]) + " " + u"\N{DEGREE SIGN}" + "C",
                "pressure": str(data["main"]["pressure"]) + "hPa",
                "humidity": str(data["main"]["humidity"]) + "%",
                "location": str(data["name"]),
                "longitude": str(data["coord"]["lon"]),
                "latitude": str(data["coord"]["lat"])
            }
        else:
            weather_data = {}
        return weather_data

    def make_api_request(self, location):
        api_url = self.configuration.get("api_url")
        api_key = self.configuration.get("api_key")
        api_endpoint = f"{api_url}?units=metric&q={location}&appid={api_key}"
        response = requests.get(api_endpoint)
        print(api_endpoint)
        return response

    def update_weather_labels(self, weather_data):
        """Updates the GUI elements with current weather data."""
        if weather_data != {}:
            self.window.location_label.config(text=f"Location: {weather_data['location']}")
            self.window.temperature_label.config(text=f"Temperature: {weather_data['temperature']}")
            self.window.pressure_label.config(text=f"Pressure: {weather_data['pressure']}")
            self.window.humidity_label.config(text=f"Humidity: {weather_data['humidity']}")
            self.window.longitude_label.config(text=f"Longitude: {weather_data['longitude']}")
            self.window.latitude_label.config(text=f"Latitude: {weather_data['latitude']}")
            self.window.location_sv.set("Search location...")
            self.window.location_entry.icursor("18")
        else:
            messagebox.showerror("Error", "Error occurred!\nEnter a valid location or check your API key!")

    def show_on_map(self):
        """Display the specified location on a map using Folium and open it in the default web browser."""
        longitude = self.window.longitude_label["text"].split(" ")[1]
        latitude = self.window.latitude_label["text"].split(" ")[1]
        if longitude != "" or latitude != "":
            map = folium.Map(location=[latitude, longitude], zoom_start=13)
            marker_text = "<font face='Bahnschrift'>Weather forecast location</font>"
            iframe = folium.IFrame(marker_text, width=220, height=35)
            popup = folium.Popup(iframe, min_width=220, max_width=220)
            folium.Marker([latitude, longitude], popup=popup, icon=folium.Icon("blue")).add_to(map)
            map.save("map.html")
            map_html = "map.html"
            webbrowser.open("file://" + os.path.realpath(map_html))
        else:
            messagebox.showerror("Error", "Search for a location first!")

    def open_settings(self):
        settings_window = SettingsWindow(self.window)
