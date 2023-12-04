import sys
import xml.etree.ElementTree as etree

def child_attrib(li):
    mylist = []; length = 0
    for i in range(len(li)):
        length += len(li[i].attrib)
        child = li[i].getchildren()
        if child:
            mylist.extend(li[i].getchildren())
    return length, mylist

def get_attr_number(root):

    li = root.getchildren()
    length = len(root.attrib)
    while li:
        leng, li = child_attrib(li)
        length += leng
    return length        
    
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print (get_attr_number(root))
