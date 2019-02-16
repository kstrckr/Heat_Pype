import tkinter as tk
from tkinter import ttk

class Text_Tab(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        self.text_entry = tk.Text(self, width=48, height=10)
        self.text_entry.grid(padx=10, pady=10)