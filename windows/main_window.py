import tkinter as tk
from PIL import Image, ImageTk

from event_handlers.main_window_event_handler import MainWindowEventHandler


class MainWindow(tk.Tk):
    """Application main window."""

    def __init__(self):
        """Initializes main window. Sets up the properties, font styles and widgets."""
        super().__init__()
        self.title("WeatherApp")
        self.iconbitmap("images/app_icon.ico")
        self.geometry("400x410")
        self.resizable(False, False)
        self.configure(bg="#d1d1d1")
        self.n_font_style = ("Bahnschrift", "11", "normal")
        self.b_font_style = ("Bahnschrift", "11", "bold")
        self.event_handler = MainWindowEventHandler(self)

        self.location_label = tk.Label(self, text="Location: ", font=self.b_font_style, bg="#398ccc")
        self.location_label.pack(fill="x")

        self.weather_icon_image = ImageTk.PhotoImage(Image.open("images/app_icon.ico"))
        self.weather_icon_label = tk.Label(self, image=self.weather_icon_image, bg="#d1d1d1")
        self.weather_icon_label.pack(pady=5)

        self.temperature_label = tk.Label(self, text="Temperature: ", font=self.n_font_style, bg="#d1d1d1")
        self.temperature_label.pack()

        self.pressure_label = tk.Label(self, text="Pressure: ", font=self.n_font_style, bg="#d1d1d1")
        self.pressure_label.pack()

        self.humidity_label = tk.Label(self, text="Humidity: ", font=self.n_font_style, bg="#d1d1d1")
        self.humidity_label.pack()

        self.wind_label = tk.Label(self, text="Wind: ", font=self.n_font_style, bg="#d1d1d1")
        self.wind_label.pack()

        self.longitude_label = tk.Label(self, text="Longitude: ", font=self.n_font_style, bg="#d1d1d1")
        self.longitude_label.pack()

        self.latitude_label = tk.Label(self, text="Latitude: ", font=self.n_font_style, bg="#d1d1d1")
        self.latitude_label.pack()

        self.location_sv = tk.StringVar()
        self.location_sv.set("Search location...")
        self.location_entry = tk.Entry(self, textvariable=self.location_sv, font=self.n_font_style, width=25)
        self.location_entry.pack(pady=(10, 0))
        self.location_entry.bind("<Button-1>", self.event_handler.clear_location_entry)

        self.check_weather_button = tk.Button(self, text="Check weather",
                                              command=lambda: self.event_handler.check_weather(location=self.event_handler.get_sv_value(self.location_sv)),
                                              font=self.b_font_style, width=25, relief="groove", bg="#398ccc", cursor="hand2")
        self.check_weather_button.pack(pady=(10, 0))
        self.bind("<Return>", lambda event: self.event_handler.check_weather(location=self.event_handler.get_sv_value(self.location_sv), event=event))

        self.show_on_map_button = tk.Button(self, text="See location on the map", command=self.event_handler.show_on_map, font=self.b_font_style, width=25,
                                            relief="groove", bg="#398ccc", cursor="hand2")
        self.show_on_map_button.pack(pady=(10, 0))

        self.settings_button = tk.Button(self, text="Settings", command=self.event_handler.open_settings, font=self.b_font_style, width=25,
                                         relief="groove", bg="#398ccc", cursor="hand2")
        self.settings_button.pack(pady=(10, 0))

        self.info_icon_image = ImageTk.PhotoImage(Image.open("images/info_icon.png"))
        self.info_icon_label = tk.Label(self, image=self.info_icon_image, bg="#d1d1d1", cursor="hand2")
        self.info_icon_label.pack(side="bottom", anchor="se")
        self.info_icon_label.bind("<Button-1>", self.event_handler.open_about)

        self.event_handler.check_weather(self.event_handler.get_value_from_configuration("default_location"))
