import tkinter as tk
from PIL import ImageTk, Image


class AboutWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("About")
        self.iconbitmap("images/app_icon.ico")
        self.geometry("460x130")
        self.resizable(False, False)
        self.configure(bg="#d1d1d1")
        self.n_font_style = ("Bahnschrift", "10", "normal")
        self.b_font_style = ("Bahnschrift", "10", "bold")

        self.app_icon_image = ImageTk.PhotoImage(Image.open("images/app_icon.ico"))
        self.app_icon = tk.Label(self, image=self.app_icon_image, bg="#d1d1d1")
        self.app_icon.pack(pady=3)

        self.first_label = tk.Label(self, text="WeatherApp", font=self.b_font_style, bg="#d1d1d1")
        self.first_label.pack()

        self.second_label = tk.Label(self, text="Created by emilian-klein (www.github.com/emilian-klein).", font=self.n_font_style, bg="#d1d1d1")
        self.second_label.pack()

        self.third_label = tk.Label(self, text="Weather data provided by OpenWeather company (www.openweather.co.uk).", font=self.n_font_style, bg="#d1d1d1")
        self.third_label.pack()

        self.transient(parent)
        self.grab_set()
        parent.wait_window(self)
