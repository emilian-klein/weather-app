import tkinter as tk


class SettingsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Settings")
        self.iconbitmap("images/main_icon.ico")
        self.geometry("400x100")
        self.resizable(False, False)
        self.font_style = ("Bahnschrift", "11", "normal")
        self.event_handler =

        self.top_frame = tk.Frame(self)
        self.top_frame.pack(fill="x", pady=10)

        self.api_key_label = tk.Label(self.top_frame, text="API Key", font=self.font_style)
        self.api_key_label.pack(side="left", padx=5)

        self.api_key_sv = tk.StringVar()
        self.api_key_sv.set("")
        self.api_key_entry = tk.Entry(self.top_frame, textvariable=self.api_key_sv, font=self.font_style, width=38)
        self.api_key_entry.pack(side="left", padx=5)

        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.pack()

        self.save_button = tk.Button(self, text="Save", command=self.destroy, font=self.font_style, width=15, relief="groove", bg="#2884C6", cursor="hand2")
        self.save_button.pack(side="left", padx=(60, 0))

        self.close_button = tk.Button(self, text="Close", command=self.destroy, font=self.font_style, width=15, relief="groove", bg="#787878", cursor="hand2")
        self.close_button.pack(side="right", padx=(0, 60))
