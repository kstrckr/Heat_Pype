import tkinter as tk
from tkinter import ttk

class Footer():

    def __init__(self, parent, *args, **kwargs):
        self.print_button = ttk.Button(parent, text="Print", command=kwargs['print_command'])
        self.print_button.grid(column=0, row=2, sticky=(tk.W, tk.E), padx=10, pady=10)

        self.clear_button = ttk.Button(parent, text="Clear", command=kwargs['clear_command'])
        self.clear_button.grid(column=1, row=2, sticky=(tk.W, tk.E), padx=10, pady=10)