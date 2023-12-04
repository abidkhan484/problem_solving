import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth

    def makeList(li):
        mylist = []
        for i in range(len(li)):
            t = li[i].getchildren()
            if t:
                mylist.extend(t)
        return mylist

    li = elem.getchildren()
    while li:
        maxdepth += 1
        li = makeList(li)

# if __name__ == '__main__':
n = int(input())
xml = ""
for i in range(n):
    xml =  xml + input() + "\n"
tree = etree.ElementTree(etree.fromstring(xml))
depth(tree.getroot(), -1)
print(maxdepth)

'''
# editorial solution:

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    if maxdepth < level:
        maxdepth = level
    for child in elem:
        depth(child, level)

'''
