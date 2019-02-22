import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

from pyprint.imageprocessing import Pil_Image

class Raster_Tab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        for col in range(0,4):
            self.columnconfigure(col, weight=1)

        self.rowconfigure(3, weight=1)
        
        self.rotate_left_button = ttk.Button(self, text="Left", command=lambda: self.rotate(-1))
        self.rotate_left_button.grid(column=0, row=0, ipady=15, padx=30, ipadx=15, pady=30, sticky=(tk.N))

        self.open_button = ttk.Button(self, text="Select Image", command=self.get_image_path)
        self.open_button.grid(column=0, row=1, ipady=15, padx=30, ipadx=15, pady=30, sticky=(tk.N))

        self.rotate_right_button = ttk.Button(self, text="Right", command=lambda: self.rotate(1))
        self.rotate_right_button.grid(column=0, row=2, ipady=15, padx=30, ipadx=15, pady=30, sticky=(tk.N))

        self.source_canvas = tk.Canvas(self, width=475)
        self.source_canvas.grid(column=1, row=0, rowspan=4, padx=10, pady=10 )

        self.processed_canvas = tk.Canvas(self, width=475)
        self.processed_canvas.grid(column=3, row=0, rowspan=4, padx=10, pady=10)

    def get_image_path(self):
        self.file_path = fd.askopenfile()
        self.pm = Pil_Image(self.file_path.name)
        self.update_preview()

    def rotate(self, direction):
        if direction < 0:
            self.pm.rotate_image(90)
            self.update_preview()
        else:
            self.pm.rotate_image(-90)
            self.update_preview()

    def update_preview(self):
        self.source_imng = self.pm.sourceImage
        self.processed_img = self.pm.tkImage
        self.source_canvas.create_image(0, 0, image=self.source_imng, anchor=tk.NW)
        self.processed_canvas.create_image(0, 0, image=self.processed_img, anchor=tk.NW)
        
        height = self.pm.tkImage.height() if self.pm.tkImage.height() < 600 else 600
        self.processed_canvas.configure(height=height)
        self.source_canvas.configure(height=height)
        