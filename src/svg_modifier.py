import xml.etree.ElementTree as ET


def load_svg(file_path):
    # load in the svg file then return xml tree and root
    tree = ET.parse(file_path)
    root = tree.getroot()
    return tree, root


def save_svg(tree, file_path):
    # save an xml tree to a svg file
    tree.write(file_path)
