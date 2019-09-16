types = ["integer", "long", "double", "float", "boolean", "liststring", "string", "anyURI"]

class Attribute:
    def __init__(self, id, title, type):
        self.id = check_instance_id(id)
        self.title = check_instance_title(title)
        self.type = check_instance_type(type)

def check_instance_id(id):
    if id is None:
        return ""
    else:
        return str(id)

def check_instance_title(name):
    if name is None:
        return ""
    else:
        return str(name)

def check_instance_type(type):
    if type is None:
        return "integer"
    elif type not in types:
        return "integer"
    else:
        return str(type)
