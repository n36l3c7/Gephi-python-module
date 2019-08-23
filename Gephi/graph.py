from Gephi.node import Node

versions = ["1.1", "1.2"]
modes = ["static", "dynamic"]
default_edge_types = ["directed", "undirected", "mutual"]


class Graph:

    # Instance
    def __init__(self, version, creator, description, mode, default_edge_type):
        self.version = check_instance_version(version)
        self.creator = check_instance_creator(creator)
        self.description = check_instance_description(description)
        self.mode = check_instance_mode(mode)
        self.default_edge_type = check_instance_default_edge_type(default_edge_type)
        self.nodes = list()
        self.edges = list()

    # Node
    def add_node(self, node):
        if self.node_exist(node):
            print("Node already exist\n")
        elif self.node_id_exist(node):
            print("Node id already exist\n")
        else:
            self.nodes.append(node)

    def remove_node(self, node):
        if self.node_exist(node):
            self.nodes.remove(node)
        else:
            print("Node doesn't exist\n")

    def node_exist(self, node):
        return any(n.return_to_string() == node.return_to_string() for n in self.nodes)

    def node_id_exist(self, node):
        if type(node) is Node:
            return any(n.id == node.id for n in self.nodes)
        elif type(node) is str:
            return any(n.id == node for n in self.nodes)

    # Edge
    def add_edge(self, edge):
        if self.edge_exist(edge):
            print("Edge already exist\n")
        elif self.edge_association_exist(edge):
            print("Edge source/target association already exist\n")
        elif not self.node_id_exist(edge.source):
            print("Doesn't exist an association between edge source and a node id\n")
        elif not self.node_id_exist(edge.target):
            print("Doesn't exist an association between edge target and a node id\n")
        else:
            self.edges.append(edge)

    def remove_edge(self, edge):
        if self.edge_exist(edge):
            self.edges.remove(edge)
        else:
            print("Edge doesn't exist\n")

    def edge_exist(self, edge):
        return any(e.return_to_string() == edge.return_to_string() for e in self.edges)

    def edge_association_exist(self, edge):
        return any(e.source == edge.source and e.target == edge.target for e in self.edges)


def check_instance_version(version):
    if version is None:
        return "1.2"
    elif version not in versions:
        return "1.2"
    else:
        return version


def check_instance_creator(creator):
    if creator is None:
        return None
    else:
        return str(creator)


def check_instance_description(description):
    if description is None:
        return None
    else:
        return str(description)


def check_instance_mode(mode):
    if mode is None:
        return "static"
    elif mode not in modes:
        return "static"
    else:
        return mode


def check_instance_default_edge_type(default_edge_type):
    if default_edge_type is None:
        return "directed"
    elif default_edge_type not in default_edge_types:
        return "directed"
    else:
        return default_edge_type

