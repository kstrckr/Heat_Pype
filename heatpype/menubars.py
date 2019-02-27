import tkinter as tk
from tkinter import ttk


class PyPrintMenus(tk.Menu):

    def __init__(self, parent):
        super().__init__(parent)

        self.menu_file = tk.Menu(self)
        
        self.add_cascade(menu=self.menu_file, label='File')
        self.menu_file.add_command(label='Quit', command=exit)

        # self.menu_edit = tk.Menu(self)
        # self.add_cascade(menu=self.menu_edit, label='Edit')