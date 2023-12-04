class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)
    
    def total(self, tree):
        temp = tree
        tmp = tree
        su = 0
        while temp:
            su += temp.data
            temp = temp.left
        while tmp:
            su += tmp.data
            tmp = tmp.right
        return (su - tree.data)



t = Tree(23)
t.left = Tree(20)
t.right = Tree(25)
t.left.left = Tree(15)
t.left.right = Tree(22)
t.right.left = Tree(23)
t.right.right = Tree(27)

# t = Tree(23, Tree(20, Tree(15), Tree(22)), Tree(25, Tree(23), Tree(27)))
