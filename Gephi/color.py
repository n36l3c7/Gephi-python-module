from Gephi.method import secure_instance


class Color:
    def __init__(self, r, g, b):
        self.r = secure_instance(check_value_color(r), "0")
        self.g = secure_instance(check_value_color(g), "0")
        self.b = secure_instance(check_value_color(b), "0")

    def return_to_string(self):
        return "R: " + str(self.r) + " | G: " + str(self.g) + " | B: " + str(self.b)

    def to_string(self):
        print("R: " + str(self.r) + " | G: " + str(self.g) + " | B: " + str(self.b))


def check_value_color(value):
    if str(value).isdigit() is False:
        return "0"
    elif int(value) < 0 or int(value) > 255:
        return "0"
    else:
        return value
