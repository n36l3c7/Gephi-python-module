from Gephi.method import secure_instance
from Gephi.color import Color
from Gephi.position import Position


class Node:
    def __init__(self, id, name, color, position, size, shape):
        self.id = check_instance_id(id)
        self.name = check_instance_name_(name)
        self.color = check_instance_color(color)
        self.position = check_instance_position(position)
        self.size = check_instance_size(size)
        self.shape = check_instance_shape(shape)

    def return_to_string(self):
        return "Id: " + str(self.id) + " | Name: " + str(self.name) + " | Color: {" + self.color.return_to_string() + "}" + " | Position :  {" + self.position.return_to_string() + "}"

    def to_string(self):
        print("Id: " + str(self.id) + " | Name: " + str(self.name) + " | Color: {" + self.color.return_to_string() + "}" + " | Position :  {" + self.position.return_to_string() + "}")


def check_instance_id(id):
    if id is None:
        return ""
    else:
        return id


def check_instance_name_(name):
    if name is None:
        return ""
    else:
        return name


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
        return size


def check_instance_shape(shape):
    if shape is None:
        return None
    else:
        return shape
