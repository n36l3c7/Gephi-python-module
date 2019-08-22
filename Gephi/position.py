from Gephi.method import secure_instance


class Position:
    def __init__(self, x, y, z):
        self.x = secure_instance(x, "")
        self.y = secure_instance(y, "")
        self.z = secure_instance(z, "")

    def return_to_string(self):
        return "X: " + str(self.x) + " | Y: " + str(self.y) + " | Z: " + str(self.z)

    def to_string(self):
        print("X: " + str(self.x) + " | Y: " + str(self.y) + " | Z: " + str(self.z))