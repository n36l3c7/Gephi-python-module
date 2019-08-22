import xml.etree.ElementTree as ET


class Graph:

    def __init__(self, version, creator, description, mode, edge_type):
        self.version = secure_instance(self.version, version, "1.2")
        self.creator = secure_instance(self.creator, creator, "")
        self.description = secure_instance((self.description, description, ""))
        self.mode = secure_instance(self.mode, mode, "static")
        self.edge_type = secure_instance(self.edge_type, edge_type, "directed")
        self.nodes = list()
        self.edges = list()

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def remove_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)

    def add_edge(self, edge):
        if edge not in self.edges:
            self.edges.append(edge)

    def remove_edge(self, edge):
        if edge in self.edges:
            self.edges.remove(edge)


class Node:
    def __init__(self, id, name, color, position, size, shape):
        self.id = secure_instance(self.id, id, "")
        self.name = secure_instance(self.name, name, "")
        self.color = secure_instance(self.color, color, Color("0", "0", "0"))
        self.position = secure_instance(self.position, position, Position("0", "0", "0"))
        self.size = secure_instance(self.size, size, "")
        self.shape = secure_instance(self.shape, shape, "")

    def return_to_string(self):
        return "Id: " + str(self.id) + " | Name: " + str(self.name) + " | Color: {" + self.color.return_to_string() + "}" + " | Position :  {" + self.position.return_to_string() + "}"

    def to_string(self):
        print("Id: " + str(self.id) + " | Name: " + str(self.name) + " | Color: {" + self.color.return_to_string() + "}" + " | Position :  {" + self.position.return_to_string() + "}")


class Edge:
    def __init__(self, id, source, target):
        self.id = secure_instance(self.id, id, "")
        self.source = secure_instance(self.source, source, "")
        self.target = secure_instance(self.target, target, "")

    def return_to_string(self):
        return "Id: " + str(self.id) + " | Source: " + str(self.source) + " | Target: " + str(self.target)

    def to_string(self):
        print("Id: " + str(self.id) + " | Source: " + str(self.source) + " | Target: " + str(self.target))


class Color:
    def __init__(self, r, g, b):
        self.r = secure_instance(self.r, r, "0")
        self.g = secure_instance(self.g, g, "0")
        self.b = secure_instance(self.b, b, "0")

    def return_to_string(self):
        return "R: " + str(self.r) + " | G: " + str(self.g) + " | B: " + str(self.b)

    def to_string(self):
        print("R: " + str(self.r) + " | G: " + str(self.g) + " | B: " + str(self.b))


class Position:
    def __init__(self, x, y, z):
        self.x = secure_instance(self.x, x, "")
        self.y = secure_instance(self.y, y, "")
        self.z = secure_instance(self.z, z, "")

    def return_to_string(self):
        return "X: " + str(self.x) + " | Y: " + str(self.y) + " | Z: " + str(self.z)

    def to_string(self):
        print("X: " + str(self.x) + " | Y: " + str(self.y) + " | Z: " + str(self.z))


###############################################
###############################################

def create_gexf_file(data, filename):
    root = ET.Element("gefx")
    if data.version is not None:
        root.attrib['version'] = data.version

    meta = ET.SubElement(root, "meta")
    if data.creator is not None:
        creator = ET.SubElement(meta, "creator")
        creator.text = data.creator
    if data.description is not None:
        description = ET.SubElement(meta, "description")
        description.text = data.description

    graph = ET.SubElement(root, "graph")
    if data.mode is not None:
        graph.attrib["mode"] = data.mode
    if data.edge_type is not None:
        graph.attrib["defaultedgetype"] = data.edge_type

    nodes = ET.SubElement(graph, "nodes")

    for n in data.nodes:
        node = ET.SubElement(nodes, "node")
        node.attrib["id"] = n.id
        node.attrib["label"] = n.name
        if n.color is not None:
            color = ET.SubElement(node, "color")
            color.attrib["r"] = n.color.r
            color.attrib["g"] = n.color.g
            color.attrib["b"] = n.color.b
        if n.position is not None:
            position = ET.SubElement(node, "position")
            position.attrib["x"] = n.position.x
            position.attrib["y"] = n.position.y
            position.attrib["z"] = n.position.z
        if n.size is not None:
            size = ET.SubElement(node, "size")
            size.attrib["value"] = n.size
        if n.shape is not None:
            shape = ET.SubElement(node, "shape")
            shape.attrib["value"] = n.shape

    edges = ET.SubElement(graph, "edges")

    for e in data.edges:
        edge = ET.SubElement(edges, "edge")
        edge.attrib["id"] = e.id
        edge.attrib["source"] = e.source
        edge.attrib["target"] = e.target

    tree = ET.ElementTree(root)
    tree.write(filename)


def import_from_gefx(filename):
    return


def secure_instance(value_to_check, get_value, default_value):
    if value_to_check is None:
        return default_value
    else:
        return get_value
