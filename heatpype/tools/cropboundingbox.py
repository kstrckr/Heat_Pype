

class Crop_Bounding_Box:
    def __init__(self, initial_x, initial_y):
        self.initial_x = initial_x
        self.initial_y = initial_y

        self.dynamic_x = initial_x
        self.dynamic_y = initial_y

        self.reference_x = (self.initial_x + self.dynamic_x) / 2
        self.reference_y = (self.initial_y + self.dynamic_y) / 2

    def __str__(self):
        width = self.dynamic_x - self.initial_x
        height = self.dynamic_y - self.initial_y
        str_output = "({}, {}) ({}, {}) width:{} height:{}".format(self.initial_x, self.initial_y, self.dynamic_x, self.dynamic_y, width, height)
        return str_output

    def update_dynamic_point(self, new_x, new_y):
        self.dynamic_x = new_x
        self.dynamic_y = new_y

    def set_reference_point(self, ref_x, ref_y):
        self.reference_x = ref_x
        self.reference_y = ref_y

    def update_all_points(self, delta_x, delta_y):
        self.initial_x += delta_x
        self.initial_y += delta_y
        self.dynamic_x += delta_x
        self.dynamic_y += delta_y
        self.reference_x += delta_x
        self.reference_y += delta_y

    def get_points(self):
        return ((self.initial_x, self.initial_y),(self.dynamic_x, self.dynamic_y))

    def return_ordered_coordinates(self):
        x_a, y_a = (self.initial_x, self.initial_y)
        x_b, y_b = (self.dynamic_x, self.dynamic_y)
        width = x_b - x_a
        height = y_b - y_a

        min_x = x_a if width > 0 else x_a + width
        min_y = y_a if height > 0 else y_a + height
        max_x = x_b if width > 0 else x_a
        max_y = y_b if height > 0 else y_a

        return (min_x, min_y, max_x, max_y)