from Gephi.method import secure_instance


class Graph:

    def __init__(self, version, creator, description, mode, edge_type):
        self.version = secure_instance(version, "1.2")
        self.creator = secure_instance(creator, "")
        self.description = secure_instance(description, "")
        self.mode = secure_instance(mode, "static")
        self.edge_type = secure_instance(edge_type, "directed")
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
