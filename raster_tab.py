import tkinter as tk
from tkinter import ttk

class Raster_Tab(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.raster_canvas = tk.Canvas(self, width=475, height=206)
        
        self.imgobj = tk.PhotoImage(file="monobmp.gif")

        self.raster_canvas.create_image(0, 0, image=self.imgobj, anchor=tk.NW)
        self.raster_canvas.grid(column=0, row=0, padx=10, pady=10)