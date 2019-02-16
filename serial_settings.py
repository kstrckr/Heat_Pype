import serial
import serial.tools.list_ports
import tkinter as tk
from tkinter import ttk

class Serial_Settings(ttk.Frame):

    rates = [
        1200,
        1400,
        4800,
        19200,
        38400,
        57600,
        115200
    ]

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.active_coms = self.return_active_coms()
        
        ttk.Label(parent, text="Serial Settings:").grid(column=0, row=0, sticky=(tk.W, tk.E), pady=5)
        


    def return_active_coms(self):
        ports = serial.tools.list_ports.comports()
        return ports
