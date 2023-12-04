import sys
import xml.etree.ElementTree as etree

def get_attr_number(root):
    # here root is iterable; check the for loop
    return len(root.attrib)+sum(get_attr_number(node) for node in root)

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
