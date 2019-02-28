import tkinter as tk
from tkinter import ttk

class PrintButtons(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):

        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.print_button = ttk.Button(self, text="Print")
        self.print_button.grid(column=0, row=0, sticky=(tk.E, tk.S, tk.W), ipady=10, padx=10)

        self.clear_button = ttk.Button(self, text="Clear")
        self.clear_button.grid(column=1, row=0, sticky=(tk.E, tk.S, tk.W), ipady=10, padx=10)
        self.grid(kwargs)

    def bind_buttons(self, print_command, clear_command):
        self.print_button.configure(command=print_command)
        self.clear_button.configure(command=clear_command)
        