from io import BytesIO

from PIL import Image, ImageTk


class Pil_Image():

    def __init__(self, path_to_image):
        self.image_rotation = 0
        self.pil_img = Image.open(path_to_image)
        
        self.refresh_output(self.pil_img)
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
        rotated_img = self.pil_img.rotate(self.image_rotation, expand=True)
        self.refresh_output(rotated_img)


    def refresh_output(self, image_input):
        resize_dimensions = self.calculate_resize_dimensions(image_input)
        print(resize_dimensions)
        resized = image_input.resize(resize_dimensions)
        
        bw = resized.convert('1')
        
        self.tkImage = ImageTk.PhotoImage(bw)
        self.sourceImage = ImageTk.PhotoImage(resized)