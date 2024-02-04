import json
from tkinter import messagebox
from settings_window import SettingsWindow

class EventHandler:
    def __init__(self, window):
        self.window = window
        self.configuration = None

    def enable_button(self, button):
        """
        Enables button by changing its state, color and cursor.
        """
        self.window.button.configure(bg="#3195DC", state="normal", cursor="hand2")

    def disable_button(self, button):
        """
        Disables button by changing its state, color and cursor.
        """
        self.window.button.configure(bg="#787878", state="disabled", cursor="x_cursor")

    def clear_location_entry(self, event):
        """
        Clears the location entry widget when clicked.
        """
        self.app.location_entry.delete(0, "end")

    def check_weather(self):
        messagebox.showinfo("Info", "Check weather.")

    def show_on_map(self):
        messagebox.showinfo("Info", "Show on map.")

    def open_settings(self):
        settings_window = SettingsWindow(self.app)

    def get_configuration(self):
        """
        Reads the 'configuration.json' file and stores the configuration details in the 'configuration' attribute.
        """
        with open("configuration.json") as file:
            self.configuration = json.load(file)
    #
    # def check_weather(self):
    #     """
    #     Updates the GUI elements with current weather data.
    #     """
    #     weather_data = self.get_weather_data()
    #     if weather_data != {}:
    #         self.location_label.config(text=f"Location: {weather_data['location']}")
    #         self.longitude_label["text"] = f"Longitude: {weather_data['longitude']}"
    #         self.latitude_label["text"] = f"Latitude: {weather_data['latitude']}"
    #         self.temperature_label["text"] = f"Temperature: {weather_data['temperature']}"
    #         self.pressure_label["text"] = f"Pressure: {weather_data['pressure']}"
    #         self.humidity_label["text"] = f"Humidity: {weather_data['humidity']}"
    #         self.location_entry_sv.set("Search for...")
    #         self.location_entry.icursor(13)
    #     else:
    #         messagebox.showwarning("Error", "Error occurred!\nEnter a valid location or check if your API key is active!")
    #
    # def get_weather_data(self):
    #     """
    #     Retrieve weather data for the specified location from the OpenWeather API.
    #     """
    #     response = requests.get(self.api_url.format(location_name=self.location_entry_sv.get(), api_key=self.configuration["api_key"]))
    #     data = response.json()
    #     if response.status_code == 200:
    #         weather_data = {
    #             "location": self.location_entry_sv.get().title(),
    #             "longitude": data["coord"]["lon"],
    #             "latitude": data["coord"]["lat"],
    #             "temperature": str(data["main"]["temp"]) + " " + u"\N{DEGREE SIGN}" + "C",
    #             "pressure": str(data["main"]["pressure"]) + "hPa",
    #             "humidity": str(data["main"]["humidity"]) + "%"
    #         }
    #     else:
    #         weather_data = {}
    #
    #     return weather_data
    #
    # def show_location_on_map(self):
    #     """
    #     Display the specified location on a map using Folium and open it in the default web browser.
    #     """
    #     longitude = self.longitude_label["text"].split(" ")[1]
    #     latitude = self.latitude_label["text"].split(" ")[1]
    #     if longitude != "" or latitude != "":
    #         map = folium.Map(location=[latitude, longitude], zoom_start=13)
    #         marker_text = "<font face='Bahnschrift'>Weather forecast location</font>"
    #         iframe = folium.IFrame(marker_text, width=220, height=35)
    #         popup = folium.Popup(iframe, min_width=220, max_width=220)
    #         folium.Marker([latitude, longitude], popup=popup, icon=folium.Icon("blue")).add_to(map)
    #         map.save("map.html")
    #         map_html = "map.html"
    #         webbrowser.open("file://" + os.path.realpath(map_html))
    #     else:
    #         messagebox.showwarning("Error", "Search for a location first!")