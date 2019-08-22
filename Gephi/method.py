import xml.etree.ElementTree as ET


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


def secure_instance(get_value, default_value):
    if get_value is None:
        return default_value
    else:
        return get_value
