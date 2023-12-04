import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    total = 0
    total += len(node.attrib)
    for i in node:
        total += len(i.attrib)

    return total

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()

    print(get_attr_number(root))
