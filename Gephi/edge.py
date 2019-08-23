types = ["directed", "undirected", "mutual"]


class Edge:
    def __init__(self, id, label, type, source, target, weight):
        self.id = check_instance_id(id)
        self.label = check_instance_label(label)
        self.type = check_instance_type(type)
        self.source = check_instance_source(source)
        self.target = check_instance_target(target)
        self.weight = check_instance_weight(weight)

    def return_to_string(self):
        string = ""
        if self.id is not None:
            string += "Id: " + self.id

        if self.label is not None:
            string += " | Label: " + self.label

        if self.type is not None:
            string += " | Type: " + self.type

        if self.source is not None:
            string += " | Source: " + self.source

        if self.target is not None:
            string += " | Target: " + self.target

        if self.weight is not None:
            string += " | Weight: " + self.weight

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


def check_instance_type(type):
    if type is None:
        return "directed"
    elif type not in types:
        return "directed"
    else:
        return str(type)


def check_instance_source(source):
    if source is None:
        return ""
    else:
        return str(source)


def check_instance_target(target):
    if target is None:
        return ""
    else:
        return str(target)


def check_instance_weight(weight):
    if weight is None:
        return None
    elif not str(weight).isdigit:
        return None
    else:
        return str(weight)
