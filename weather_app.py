import tkinter as tk
from tkinter import messagebox
import requests
import json
import folium
import webbrowser
import os


class WeatherApp(tk.Tk):
    def __init__(self):
        """
        Initialize the WeatherApp Tkinter application.

        Sets up the window properties, font styles, and initializes attributes.
        """
        super().__init__()
        self.title("Weather App")
        self.iconbitmap("images/icon.ico")
        self.geometry("400x280")
        self.resizable(False, False)
        self.n_font_style = ("Bahnschrift", "11", "normal")
        self.b_font_style = ("Bahnschrift", "11", "bold")
        self.configuration = None
        self.api_url = "https://api.openweathermap.org/data/2.5/weather?q={location_name}&units=metric&appid={api_key}"

        self.location_label = tk.Label(self, text="Location: ", bg="steelblue3", font=self.b_font_style)
        self.longitude_label = tk.Label(self, text="Longitude: ", font=self.b_font_style)
        self.latitude_label = tk.Label(self, text="Latitude: ", font=self.b_font_style)
        self.temperature_label = tk.Label(self, text="Temperature: ", font=self.b_font_style)
        self.pressure_label = tk.Label(self, text="Pressure: ",  font=self.b_font_style)
        self.humidity_label = tk.Label(self, text="Humidity: ", font=self.b_font_style)

        self.location_entry_sv = tk.StringVar()
        self.location_entry_sv.set("Search city...")
        self.location_entry = tk.Entry(self, textvariable=self.location_entry_sv, font=self.n_font_style, width=25)
        self.location_entry.bind("<Button-1>", self.clear_location_entry)

        self.check_weather_button = tk.Button(self, text="Check weather", command=self.check_weather, font=self.n_font_style, relief="groove",
                                              bg="steelblue3", width=25, cursor="hand2")
        self.show_on_map_button = tk.Button(self, text="See location on the map", command=self.show_location_on_map, font=self.n_font_style,
                                            relief="groove", bg="steelblue3", width=25, cursor="hand2")

        self.location_label.pack(fill="x")
        self.longitude_label.pack(fill="x")
        self.latitude_label.pack(fill="x")
        self.temperature_label.pack(fill="x")
        self.pressure_label.pack(fill="x")
        self.humidity_label.pack(fill="x")
        self.location_entry.pack(pady=(10, 0))
        self.check_weather_button.pack(pady=(10, 0))
        self.show_on_map_button.pack(pady=(10, 0))

    def clear_location_entry(self, event):
        """
        Clear the location entry widget when clicked.

        Parameters:
        - event (tk.Event): The event triggered by clicking on the location entry widget.
        """

        self.location_entry.delete(0, "end")

    def get_configuration(self):
        """
        Retrieve and load configuration details from 'configuration.json'.
        Reads the 'configuration.json' file and stores the configuration details in the 'configuration' attribute.
        """
        with open("configuration.json") as file:
            self.configuration = json.load(file)

    def check_weather(self):
        """
        Check the weather for the specified location and update displayed information in the Tkinter window.
        Retrieves weather data for the specified location using the OpenWeather API and updates the GUI elements.
        """
        weather_data = self.get_weather_data()
        if weather_data != {}:
            self.location_label.config(text=f"Location: {weather_data['location']}")
            self.longitude_label["text"] = f"Longitude: {weather_data['longitude']}"
            self.latitude_label["text"] = f"Latitude: {weather_data['latitude']}"
            self.temperature_label["text"] = f"Temperature: {weather_data['temperature']}"
            self.pressure_label["text"] = f"Pressure: {weather_data['pressure']}"
            self.humidity_label["text"] = f"Humidity: {weather_data['humidity']}"
            self.location_entry_sv.set("Search for...")
            self.location_entry.icursor(13)
        else:
            messagebox.showwarning("Error", "Enter a valid location first!")

    def get_weather_data(self):
        """
        Retrieve weather data for the specified location from the OpenWeather API.

        Returns:
        - weather_data (dict): A dictionary containing weather information, or an empty dictionary if an error occurs.
        """
        response = requests.get(self.api_url.format(location_name=self.location_entry_sv.get(), api_key=self.configuration["api_key"]))
        data = response.json()
        if response.status_code == 200:
            weather_data = {
                "location": self.location_entry_sv.get().title(),
                "longitude": data["coord"]["lon"],
                "latitude": data["coord"]["lat"],
                "temperature": str(data["main"]["temp"]) + " " + u"\N{DEGREE SIGN}" + "C",
                "pressure": str(data["main"]["pressure"]) + "hPa",
                "humidity": str(data["main"]["humidity"]) + "%"
            }
        else:
            weather_data = {}

        return weather_data

    def show_location_on_map(self):
        """
        Display the specified location on a map using Folium and open it in the default web browser.
        Uses Folium to generate an HTML map with a marker for the specified location and opens it in the default web browser.
        """
        longitude = self.longitude_label["text"].split(" ")[1]
        latitude = self.latitude_label["text"].split(" ")[1]
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
            messagebox.showwarning("Error", "Search for a location first!")


if __name__ == "__main__":
    app = WeatherApp()
    app.get_configuration()
    app.mainloop()
