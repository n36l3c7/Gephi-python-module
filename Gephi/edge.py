from Gephi.method import secure_instance


class Edge:
    def __init__(self, id, source, target):
        self.id = secure_instance(id, "")
        self.source = secure_instance(source, "")
        self.target = secure_instance(target, "")

    def return_to_string(self):
        return "Id: " + str(self.id) + " | Source: " + str(self.source) + " | Target: " + str(self.target)

    def to_string(self):
        print("Id: " + str(self.id) + " | Source: " + str(self.source) + " | Target: " + str(self.target))