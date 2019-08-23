class Color:
    def __init__(self, r, g, b):
        self.r = (check_instance_color(r))
        self.g = (check_instance_color(g))
        self.b = (check_instance_color(b))

    def return_to_string(self):
        return "R: " + str(self.r) + " | G: " + str(self.g) + " | B: " + str(self.b)

    def to_string(self):
        print("R: " + str(self.r) + " | G: " + str(self.g) + " | B: " + str(self.b))


def check_instance_color(value):
    if value is None:
        return "0"
    elif str(value).isdigit() is False:
        return "0"
    elif int(value) < 0 or int(value) > 255:
        return "0"
    else:
        return value
