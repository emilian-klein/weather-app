import tkinter as tk

from event_handlers.settings_window_event_handler import SettingsWindowEventHandler


class SettingsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Settings")
        self.iconbitmap("images/app_icon.ico")
        self.geometry("420x190")
        self.resizable(False, False)
        self.configure(bg="#d1d1d1")
        self.n_font_style = ("Bahnschrift", "11", "normal")
        self.b_font_style = ("Bahnschrift", "11", "bold")
        self.event_handler = SettingsWindowEventHandler(self)

        self.api_key_frame = tk.Frame(self, bg="#d1d1d1")
        self.api_key_frame.pack(fill="x", pady=10)

        self.api_key_label = tk.Label(self.api_key_frame, text="API key", font=self.b_font_style, bg="#d1d1d1", width=13, anchor="w")
        self.api_key_label.pack(side="left", padx=5)

        self.api_key_sv = tk.StringVar()
        self.api_key_sv.set(self.event_handler.get_value_from_configuration("api_key"))
        self.api_key_entry = tk.Entry(self.api_key_frame, textvariable=self.api_key_sv, font=self.n_font_style, width=35)
        self.api_key_entry.pack(side="left", padx=5)

        self.default_location_frame = tk.Frame(self, bg="#d1d1d1")
        self.default_location_frame.pack(fill="x", pady=10)

        self.default_location_label = tk.Label(self.default_location_frame, text="Default location", font=self.b_font_style, bg="#d1d1d1", width=13, anchor="w")
        self.default_location_label.pack(side="left", padx=5)

        self.default_location_sv = tk.StringVar()
        self.default_location_sv.set(self.event_handler.get_value_from_configuration("default_location"))
        self.default_location_entry = tk.Entry(self.default_location_frame, textvariable=self.default_location_sv, font=self.n_font_style, width=35)
        self.default_location_entry.pack(side="left", padx=5)

        self.units_frame = tk.Frame(self, bg="#d1d1d1")
        self.units_frame.pack(fill="x", pady=10)

        self.units_label = tk.Label(self.units_frame, text="Units", font=self.b_font_style, bg="#d1d1d1", width=13, anchor="w")
        self.units_label.pack(side="left", padx=5)

        self.units_sv = tk.StringVar()
        self.units_sv.set(self.event_handler.get_value_from_configuration("units"))
        self.units_metric_radiobutton = tk.Radiobutton(self.units_frame, text="Metric", variable=self.units_sv, value="metric", font=self.n_font_style,
                                                       bg="#d1d1d1", activebackground="#d1d1d1")
        self.units_metric_radiobutton.pack(side="left", padx=(0, 5))
        self.units_standard_radiobutton = tk.Radiobutton(self.units_frame, text="Standard", variable=self.units_sv, value="standard", font=self.n_font_style,
                                                         bg="#d1d1d1", activebackground="#d1d1d1")
        self.units_standard_radiobutton.pack(side="left", padx=(0, 5))
        self.units_imperial_radiobutton = tk.Radiobutton(self.units_frame, text="Imperial", variable=self.units_sv, value="imperial", font=self.n_font_style,
                                                         bg="#d1d1d1", activebackground="#d1d1d1")
        self.units_imperial_radiobutton.pack(side="left", padx=(0, 5))

        self.buttons_frame = tk.Frame(self, bg="#d1d1d1")
        self.buttons_frame.pack(fill="x")

        self.save_settings_button = tk.Button(self, text="Save", command=self.event_handler.save_settings, font=self.b_font_style, width=15, relief="groove",
                                              bg="#398ccc", cursor="hand2")
        self.save_settings_button.pack(side="left", padx=(60, 0))
        self.bind("<Return>", self.event_handler.save_settings)

        self.close_settings_button = tk.Button(self, text="Close", command=self.event_handler.close_settings, font=self.b_font_style, width=15, relief="groove",
                                               bg="#787878", cursor="hand2")
        self.close_settings_button.pack(side="right", padx=(0, 60))

        self.transient(parent)
        self.grab_set()
        parent.wait_window(self)
