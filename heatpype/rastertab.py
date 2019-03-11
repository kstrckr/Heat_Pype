import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

from heatpype.tools.imageprocessing import Pil_Image
from heatpype.tools.cropboundingbox import Crop_Bounding_Box

class Raster_Tab(ttk.Frame):

    printer_width = 512

    def __init__(self, parent):
        super().__init__(parent)

        self.crop_bounding_box = None

        for col in range(0,4):
            self.columnconfigure(col, weight=1)

        self.rowconfigure(3, weight=1)
        
        self.rotate_left_button = ttk.Button(self, text="Left", command=lambda: self.rotate(-1))
        self.rotate_left_button.grid(column=0, row=0, ipady=15, padx=30, ipadx=15, pady=30, sticky=(tk.N))

        self.open_button = ttk.Button(self, text="Select Image", command=self.get_image_path)
        self.open_button.grid(column=0, row=1, ipady=15, padx=30, ipadx=15, pady=30, sticky=(tk.N))

        self.rotate_right_button = ttk.Button(self, text="Right", command=lambda: self.rotate(1))
        self.rotate_right_button.grid(column=0, row=2, ipady=15, padx=30, ipadx=15, pady=30, sticky=(tk.N))

        self.source_canvas = tk.Canvas(self, width=self.printer_width)
        self.source_canvas.grid(column=1, row=0, rowspan=4 )

        self.processed_canvas = tk.Canvas(self, width=self.printer_width)
        self.processed_canvas.grid(column=3, row=0, rowspan=4, padx=10, pady=10)

        self.source_canvas.bind("<Button-1>", self.initiate_crop)
        self.source_canvas.bind("<B1-Motion>", self.define_crop_box)
        self.source_canvas.bind("<B3-Motion>", self.translate_crop_box)
        self.source_canvas.bind("<Button-3>", self.set_translation_reference_point)

    def get_image_path(self):
        self.file_path = fd.askopenfilename()
        self.pm = Pil_Image(self.file_path)
        self.update_preview()

    def rotate(self, direction):
        if direction < 0:
            self.pm.rotate_image(90)
            self.update_preview()
        else:
            self.pm.rotate_image(-90)
            self.update_preview()
        if self.crop_bounding_box:
            self.draw_crop_box(self.crop_bounding_box)

    def define_crop_box(self, e):
        self.crop_bounding_box.update_dynamic_point(e.x, e.y)
        self.pm.apply_crop(self.crop_bounding_box)
        self.update_preview()
        self.draw_crop_box(self.crop_bounding_box)

    def initiate_crop(self, e):
        self.crop_bounding_box = Crop_Bounding_Box(e.x, e.y)

    def set_translation_reference_point(self, e):
        if self.crop_bounding_box:
            self.crop_bounding_box.sett_reference_popint(e.x, e.y)

    def translate_crop_box(self, e):
        if self.crop_bounding_box:
            ref_x = self.crop_bounding_box.reference_x
            ref_y = self.crop_bounding_box.reference_y

            if e.x > ref_x:
                delta_x = e.x - ref_x
            else:
                delta_x = 0 - (ref_x - e.x)

            if e.y > ref_y:
                delta_y = e.y - ref_y
            else:
                delta_y = 0 - (ref_y - e.y)

            self.crop_bounding_box.update_all_points(delta_x, delta_y)
            self.pm.apply_crop(self.crop_bounding_box)
            print(delta_x, delta_y)
            self.update_preview()
            self.draw_crop_box(self.crop_bounding_box)

    def draw_crop_box(self, crop_bounding_box):
        static_point, dynamic_point = self.crop_bounding_box.get_points()
        x1, y1 = static_point
        x2, y2 = dynamic_point
        self.source_canvas.delete("crop_box")
        self.source_canvas.create_rectangle((x1, y1, x2, y2), width=1, outline="white", tag="crop_box")
        self.source_canvas.create_rectangle((x1-1, y1-1, x2+1, y2+1), width=1, outline="black", tag="crop_box")

    def update_preview(self):
        self.source_imng = self.pm.sourceImage
        self.processed_img = self.pm.tkImage
        self.source_canvas.create_image(0, 0, image=self.source_imng, anchor=tk.NW)
        self.processed_canvas.create_image(0, 0, image=self.processed_img, anchor=tk.NW)
        height = self.pm.tkImage.height()
        self.processed_canvas.configure(height=height)
        self.source_canvas.configure(height=height)