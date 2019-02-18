from io import BytesIO

from PIL import Image, ImageTk


class Pil_Image():

    def __init__(self, path_to_image):
        with Image.open(path_to_image) as source_img:
            resize_dimensions = self.calculate_resize_dimensions(source_img)
            resized = source_img.resize(resize_dimensions)

            bw = resized.convert('1')
            
            self.tkImage = ImageTk.PhotoImage(bw)
            self.image_bytes = self.return_img_bytes(bw)

    def return_img_bytes(self, image):

        with BytesIO() as output:
            image.save(output, 'BMP')
            data = output.getvalue()

        return data

    def calculate_resize_dimensions(self, source_img):
        width = source_img.width
        height = source_img.height

        ratio = 475/width

        output_height = int(height*ratio)

        return (475, output_height)
