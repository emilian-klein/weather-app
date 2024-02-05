import tkinter as tk

from event_handlers.settings_window_event_handler import SettingsWindowEventHandler


class SettingsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Settings")
        self.iconbitmap("images/icon.ico")
        self.geometry("400x100")
        self.resizable(False, False)
        self.font_style = ("Bahnschrift", "11", "normal")
        self.event_handler = SettingsWindowEventHandler(self)

        self.top_frame = tk.Frame(self)
        self.top_frame.pack(fill="x", pady=10)

        self.api_key_label = tk.Label(self.top_frame, text="API Key", font=self.font_style)
        self.api_key_label.pack(side="left", padx=5)

        self.api_key_sv = tk.StringVar()
        self.api_key_sv.set(self.event_handler.set_api_key_sv())
        self.api_key_entry = tk.Entry(self.top_frame, textvariable=self.api_key_sv, font=self.font_style, width=38)
        self.api_key_entry.pack(side="left", padx=5)

        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.pack()

        self.save_api_key_button = tk.Button(self, text="Save", command=self.event_handler.save_api_key, font=self.font_style, width=15, relief="groove", bg="#2884C6", cursor="hand2")
        self.save_api_key_button.pack(side="left", padx=(60, 0))

        self.close_settings_button = tk.Button(self, text="Close", command=self.event_handler.close_settings, font=self.font_style, width=15, relief="groove", bg="#787878", cursor="hand2")
        self.close_settings_button.pack(side="right", padx=(0, 60))

        self.grab_set()
        self.wait_window(self)
