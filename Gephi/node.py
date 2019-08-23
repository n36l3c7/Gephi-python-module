from Gephi.method import secure_instance
from Gephi.color import Color
from Gephi.position import Position


class Node:
    def __init__(self, id, label, color, position, size, shape):
        self.id = check_instance_id(id)
        self.label = check_instance_label(label)
        self.color = check_instance_color(color)
        self.position = check_instance_position(position)
        self.size = check_instance_size(size)
        self.shape = check_instance_shape(shape)

    def return_to_string(self):
        string = ""
        if self.id is not None:
            string += "Id: " + self.id

        if self.label is not None:
            string += " | Label: " + self.label

        if self.color is not None:
            string += " | Color: {" + self.color.return_to_string() + "}"

        if self.position is not None:
            string += " | Position: {" + self.position.return_to_string() + "}"

        if self.size is not None:
            string += " | Size: " + self.size

        if self.shape is not None:
            string += " | Shape: " + self.shape

        return string

    def to_string(self):
        print(self.return_to_string())


def check_instance_id(id):
    if id is None:
        return ""
    else:
        return str(id)


def check_instance_label(label):
    if label is None:
        return ""
    else:
        return str(label)


def check_instance_color(color):
    if color is None:
        return None
    elif type(color) is not Color:
        return None
    else:
        return color


def check_instance_position(position):
    if position is None:
        return None
    elif type(position) is not Position:
        return None
    else:
        return position


def check_instance_size(size):
    if size is None:
        return None
    else:
        return str(size)


def check_instance_shape(shape):
    if shape is None:
        return None
    else:
        return str(shape)
