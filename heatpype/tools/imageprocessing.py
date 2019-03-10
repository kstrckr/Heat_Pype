from io import BytesIO

from PIL import Image, ImageOps, ImageTk


class Pil_Image():

    printer_width = 512

    def __init__(self, path_to_image):
        self.image_rotation = 0
        self.pil_img = Image.open(path_to_image)
        self.crop_values = None
        self.refresh_output()
        # self.image_bytes = self.return_img_bytes(bw)

    def return_printable_bytes(self):
        # inverted_img = ImageOps.invert(self.converted_output)
        return self.printable_output.tobytes()

    def return_processed_img_dimensions(self):
        return (self.converted_output.width, self.converted_output.height)

    def calculate_resize_dimensions(self, source_img):
        width = source_img.width
        height = source_img.height

        ratio = self.printer_width/width

        output_height = int(height*ratio)

        return (self.printer_width, output_height)

    def rotate_image(self, direction):
        self.image_rotation += direction
        if self.image_rotation == 360 or self.image_rotation == -360:
            self.image_rotation = 0
        
        # self.pil_img = self.pil_img.rotate(self.image_rotation, expand=True)
        self.refresh_output()

    def apply_crop(self, crop_bounding_box):
        initial_point, dynamic_point = crop_bounding_box
        x1, y1 = initial_point
        x2, y2 = dynamic_point
        self.crop_values = (x1, y1, x2, y2)
        self.refresh_output()

    def calculate_crop_ratio(self, input_img, raw_crop_values):
        ratio = input_img.width/self.printer_width

        mapped_crop = map(lambda x: x*ratio, raw_crop_values)
        return tuple(mapped_crop)


    def refresh_output(self):
        rotated_img = self.pil_img.rotate(self.image_rotation, expand=True)
        resize_dimensions = self.calculate_resize_dimensions(rotated_img)

        resized_input = rotated_img.resize(resize_dimensions)

        if self.crop_values:
            mapped_values = self.calculate_crop_ratio(rotated_img, self.crop_values)
            # print(mapped_values)
            preprocessed_input = rotated_img.crop(mapped_values).resize(resize_dimensions)
        else:
            preprocessed_input = resized_input
        
        self.printable_output = ImageOps.invert(preprocessed_input).convert('1')
        self.converted_output = preprocessed_input.convert('1')
        self.tkImage = ImageTk.PhotoImage(self.converted_output)
        self.sourceImage = ImageTk.PhotoImage(resized_input)

