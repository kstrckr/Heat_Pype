from io import BytesIO

from PIL import Image, ImageTk


class Pil_Image():

    def __init__(self, path_to_image):
        self.image_rotation = 0
        self.pil_img = Image.open(path_to_image)
        self.crop_values = None
        self.refresh_output()
        # self.image_bytes = self.return_img_bytes(bw)

    # def return_img_bytes(self, image):

    #     with BytesIO() as output:
    #         image.save(output, 'BMP')
    #         data = output.getvalue()

    #     return data

    def calculate_resize_dimensions(self, source_img):
        width = source_img.width
        height = source_img.height

        ratio = 475/width

        output_height = int(height*ratio)

        return (475, output_height)

    def rotate_image(self, direction):
        self.image_rotation += direction
        if self.image_rotation == 360 or self.image_rotation == -360:
            self.image_rotation = 0
        
        self.pil_img = self.pil_img.rotate(self.image_rotation, expand=True)
        self.refresh_output()

    def apply_crop(self, crop_bounding_box):
        initial_point, dynamic_point = crop_bounding_box
        x1, y1 = initial_point
        x2, y2 = dynamic_point
        self.crop_values = (x1, y1, x2, y2)
        print(self.crop_values)
        self.refresh_output()

    def calculate_crop_ratio(self, raw_crop_values):
        ratio = self.pil_img.width/475

        mapped_crop = map(lambda x: x*ratio, raw_crop_values)
        return tuple(mapped_crop)


    def refresh_output(self):
        resize_dimensions = self.calculate_resize_dimensions(self.pil_img)

        resized_input = self.pil_img.resize(resize_dimensions)

        if self.crop_values:
            mapped_values = self.calculate_crop_ratio(self.crop_values)
            # print(mapped_values)
            preprocessed_input = self.pil_img.crop(mapped_values).resize(resize_dimensions)
        else:
            preprocessed_input = resized_input
        
        self.tkImage = self.refresh_processed_img(preprocessed_input)
        self.sourceImage = ImageTk.PhotoImage(resized_input)

    def refresh_processed_img(self, preprocessed_img):
        bw = preprocessed_img.convert('1')
        return ImageTk.PhotoImage(bw)
