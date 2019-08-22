from Gephi.method import secure_instance
from Gephi.color import Color
from Gephi.position import Position

class Node:
    def __init__(self, id, name, color, position, size, shape):
        self.id = secure_instance(id, "")
        self.name = secure_instance(name, "")
        self.color = secure_instance(color, Color("0", "0", "0"))
        self.position = secure_instance(position, Position("0", "0", "0"))
        self.size = secure_instance(size, "")
        self.shape = secure_instance(shape, "")

    def return_to_string(self):
        return "Id: " + str(self.id) + " | Name: " + str(self.name) + " | Color: {" + self.color.return_to_string() + "}" + " | Position :  {" + self.position.return_to_string() + "}"

    def to_string(self):
        print("Id: " + str(self.id) + " | Name: " + str(self.name) + " | Color: {" + self.color.return_to_string() + "}" + " | Position :  {" + self.position.return_to_string() + "}")