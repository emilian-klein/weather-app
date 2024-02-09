import requests
import folium
import os
import webbrowser
from tkinter import messagebox

from PIL import ImageTk, Image

from event_handlers.event_handler import EventHandler
from windows.settings_window import SettingsWindow


class MainWindowEventHandler(EventHandler):
    """Class responsible for handling events which happens in main window."""

    def clear_location_entry(self, event):
        """Clears location entry widget when it is clicked with left mouse button."""
        self.window.location_entry.delete(0, "end")

    def set_default_location_entry_value(self):
        """Set default value on location entry widget."""
        self.window.location_sv.set("Search location...")
        # self.window.location_entry.icursor("18")

    def check_weather(self, event=None):
        """Updates label widgets with current weather data for specified location."""
        location = self._get_location()
        response = self.make_api_request(location)
        weather_data = self.get_data_from_api_response(response)
        self.update_weather_labels(weather_data)
        self.window.focus()

    def _get_location(self):
        """Gets value currently presented in location entry widget."""
        return str(self.window.location_entry.get())

    def make_api_request(self, location):
        """Makes request to OpenWeather API service and retrieves weather data for specific location. Shows warnings if something goes wrong."""
        self.get_configuration()
        api_url = self.configuration.get("api_url")
        api_key = self.configuration.get("api_key")
        api_endpoint = f"{api_url}?units=metric&q={location}&appid={api_key}"
        try:
            response = requests.get(api_endpoint)
            response.raise_for_status()

            return response
        except requests.HTTPError as exception:
            self.set_default_location_entry_value()
            if exception.response.status_code == 401:
                messagebox.showwarning("Warning", "Invalid API key!")
            elif exception.response.status_code == 404 or exception.response.status_code == 400:
                messagebox.showwarning("Warning", "Location was not found!")
            else:
                messagebox.showwarning("Error", f"Error: {exception}")

    def get_data_from_api_response(self, response):
        """Returns weather data as dictionary which is created from getting specific values from the API response."""
        weather_data = {}
        if response and response.status_code == 200:
            response_data = response.json()
            weather_data = {
                "location": str(response_data["name"]),
                "temperature": str(response_data["main"]["temp"]) + " " + u"\N{DEGREE SIGN}" + "C",
                "pressure": str(response_data["main"]["pressure"]) + "hPa",
                "humidity": str(response_data["main"]["humidity"]) + "%",
                "wind": str(response_data["wind"]["speed"]) + " m/s",
                "longitude": str(response_data["coord"]["lon"]),
                "latitude": str(response_data["coord"]["lat"]),
                "icon": str(response_data["weather"][0]["icon"])
            }

        return weather_data

    def update_weather_labels(self, weather_data):
        """Updates widgets with downloaded weather data."""
        if weather_data:
            self.window.location_label.config(text=f"Location: {weather_data['location']}")
            self.window.temperature_label.config(text=f"Temperature: {weather_data['temperature']}")
            self.window.pressure_label.config(text=f"Pressure: {weather_data['pressure']}")
            self.window.humidity_label.config(text=f"Humidity: {weather_data['humidity']}")
            self.window.wind_label.config(text=f"Wind: {weather_data['wind']}")
            self.window.longitude_label.config(text=f"Longitude: {weather_data['longitude']}")
            self.window.latitude_label.config(text=f"Latitude: {weather_data['latitude']}")
            self.set_default_location_entry_value()
            self.window.photo = ImageTk.PhotoImage(Image.open(f"images/weather_icons/{weather_data['icon']}.png"))
            self.window.weather_icon.configure(image=self.window.photo)

    def show_on_map(self):
        """Displays the specified location on a map in the default web browser."""
        latitude = self.window.latitude_label.cget("text").split(" ")[1]
        longitude = self.window.longitude_label.cget("text").split(" ")[1]
        if latitude and longitude:
            map = folium.Map(location=[latitude, longitude], zoom_start=13)
            marker_text = "<font face='Bahnschrift'>Weather forecast location</font>"
            iframe = folium.IFrame(marker_text, width=220, height=35)
            popup = folium.Popup(iframe, min_width=220, max_width=220)
            folium.Marker([latitude, longitude], popup=popup, icon=folium.Icon("blue")).add_to(map)
            map.save("map.html")
            map_html = "map.html"
            webbrowser.open("file://" + os.path.realpath(map_html))
        else:
            messagebox.showwarning("Warning", "Search for a location first!")

    def open_settings(self):
        """Open settings window."""
        settings_window = SettingsWindow(self.window)
