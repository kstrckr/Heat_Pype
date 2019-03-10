import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd


class PyPrintMenus(tk.Menu):

    image_path = None

    def __init__(self, parent):
        super().__init__(parent)

        self.menu_file = tk.Menu(self)
        
        self.add_cascade(menu=self.menu_file, label='File')
        self.menu_file.add_command(label='Open Image', command=self.set_image_path)
        self.menu_file.add_separator()
        self.menu_file.add_command(label='Quit', command=exit)

    def set_image_path(self):
        self.image_path = fd.askopenfilename()
        print(self.image_path)
