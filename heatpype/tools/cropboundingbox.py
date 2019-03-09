

class Crop_Bounding_Box:
    def __init__(self, initial_x, initial_y):
        self.initial_x = initial_x
        self.initial_y = initial_y

        self.dynamic_x = initial_x
        self.dynamic_y = initial_y

    def __str__(self):
        width = self.dynamic_x - self.initial_x
        height = self.dynamic_y - self.initial_y
        str_output = "({}, {}) ({}, {}) width:{} height:{}".format(self.initial_x, self.initial_y, self.dynamic_x, self.dynamic_y, width, height)
        return str_output

    def update_dynamic_point(self, new_x, new_y):
        self.dynamic_x = new_x
        self.dynamic_y = new_y

    def get_points(self):
        return ((self.initial_x, self.initial_y),(self.dynamic_x, self.dynamic_y))