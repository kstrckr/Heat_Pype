import tkinter as tk
from tkinter import ttk

import pyprint.texttab as tt
import pyprint.rastertab as rt

class Printing_Tabs(ttk.Notebook):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)

        self.raster_tab = rt.Raster_Tab(self)
        self.text_tab = tt.Text_Tab(self)
        
        self.add(self.raster_tab, text=" Raster ")
        self.add(self.text_tab, text="  Text  ")
        self.grid(kwargs)


    def Get_Text_Input(self):
        return self.text_tab.text_entry.get("1.0", tk.END)

    def Clear_Text(self):
        self.text_tab.text_entry.delete("1.0", tk.END)