import serial
import serial.tools.list_ports
import tkinter as tk
from tkinter import ttk

class Serial_Settings(ttk.Frame):

    rates = [
        1200,
        1400,
        4800,
        9600,
        19200,
        38400,
        57600,
        115200
    ]

    def __init__(self, parent, **kwargs):
        super().__init__(parent)

        self.selected_coms = tk.StringVar()
        self.selected_baud = tk.IntVar()

        self.active_coms = serial.tools.list_ports.comports()
        
        ttk.Label(self, text="Serial Settings:").grid(column=0, row=0, sticky=(tk.W, tk.E), pady=5)
        
        self.com_combobox = ttk.Combobox(self, textvariable=self.selected_coms, values=[com.device for com in self.active_coms], state="readonly")
        self.com_combobox.grid(column=1, row=1, pady=5)
        ttk.Label(self, text="COM Port").grid(column=0, row=1, sticky=(tk.W))

        ttk.Separator(self, orient=tk.HORIZONTAL).grid(column=1, row=2)

        self.baud_combobox = ttk.Combobox(self, textvariable=self.selected_baud, values=self.rates, state="readonly")
        self.baud_combobox.grid(column=1, row=3, pady=5)
        self.baud_combobox.set(38400)
        ttk.Label(self, text="Baud Rate").grid(column=0, row=3, sticky=(tk.W))

        self.set_coms_combobox_state()

        self.grid(kwargs)

    def set_coms_combobox_state(self):
        if not self.active_coms:
            self.com_combobox.configure(state='disabled')
        else:
            self.com_combobox.set(self.active_coms[0].device)
