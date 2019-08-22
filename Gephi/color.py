from Gephi.method import secure_instance


class Color:
    def __init__(self, r, g, b):
        self.r = secure_instance(r, "0")
        self.g = secure_instance(g, "0")
        self.b = secure_instance(b, "0")

    def return_to_string(self):
        return "R: " + str(self.r) + " | G: " + str(self.g) + " | B: " + str(self.b)

    def to_string(self):
        print("R: " + str(self.r) + " | G: " + str(self.g) + " | B: " + str(self.b))