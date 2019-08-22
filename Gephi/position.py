class Position:
    def __init__(self, x, y, z):
        self.x = check_value_position(x)
        self.y = check_value_position(y)
        self.z = check_value_position(z)

    def return_to_string(self):
        return "X: " + str(self.x) + " | Y: " + str(self.y) + " | Z: " + str(self.z)

    def to_string(self):
        print("X: " + str(self.x) + " | Y: " + str(self.y) + " | Z: " + str(self.z))


def check_instance_position(value):
    if value is None:
        return "0"
    elif str(value).isdigit() is False:
        return "0"
    else:
        return value;