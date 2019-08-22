import xml.etree.ElementTree as ET


class Graph:

    def __init__(self, version, creator, description, mode, edge_type):
        self.version = version
        self.creator = creator
        self.description = description
        self.mode = mode
        self.edge_type = edge_type
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

    def create_gexf_file(self, filename):
        root = ET.Element("gefx")
        if self.version is not None:
            root.attrib['version'] = self.version

        meta = ET.SubElement(root, "meta")
        if self.creator is not None:
            creator = ET.SubElement(meta, "creator")
            creator.text = self.creator
        if self.description is not None:
            description = ET.SubElement(meta, "description")
            description.text = self.description

        graph = ET.SubElement(root, "graph")
        if self.mode is not None:
            graph.attrib["mode"] = self.mode
        if self.edge_type is not None:
            graph.attrib["defaultedgetype"] = self.edge_type

        nodes = ET.SubElement(graph, "nodes")

        for n in self.nodes:
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

        for e in self.edges:
            edge = ET.SubElement(edges, "edge")
            edge.attrib["id"] = e.id
            edge.attrib["source"] = e.source
            edge.attrib["target"] = e.target

        tree = ET.ElementTree(root)
        tree.write(filename + ".gexf")


class Node:
    def __init__(self, id, name, color, position, size, shape):
        self.id = id
        self.name = name
        self.color = color
        self.position = position
        self.size = size
        self.shape = shape

    def return_to_string(self):
        return "Id: " + str(self.id) + " | Name: " + str(self.name) + " | Color: {" + self.color.return_to_string() + "}" + " | Position :  {" + self.position.return_to_string() + "}"

    def to_string(self):
        print("Id: " + str(self.id) + " | Name: " + str(self.name) + " | Color: {" + self.color.return_to_string() + "}" + " | Position :  {" + self.position.return_to_string() + "}")


class Edge:
    def __init__(self, id, source, target):
        self.id = id
        self.source = source
        self.target = target


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def return_to_string(self):
        return "R: " + str(self.r) + " | G: " + str(self.g) + " | B: " + str(self.b)

    def to_string(self):
        print("R: " + str(self.r) + " | G: " + str(self.g) + " | B: " + str(self.b))


class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def return_to_string(self):
        return "X: " + str(self.x) + " | Y: " + str(self.y) + " | Z: " + str(self.z)

    def to_string(self):
        print("X: " + str(self.x) + " | Y: " + str(self.y) + " | Z: " + str(self.z))
