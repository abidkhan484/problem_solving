class Node:
    def __init__(self,info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
'''
################################################
# this is my code

def height2(root, p=0, maxim=-1):

    if root:
        if root.left:
            p, maxim = height2(root.left, p+1, maxim)
            p -= 1
        if root.right:
            p, maxim = height2(root.right, p+1, maxim)
            p -= 1

        if p > maxim:
            maxim = p

    return p, maxim

def height(root):
    return height2(root)[-1]
'''

# this solution i get from the "editorial" after solve with the code above.
# i just need to know how this (below) code works
def height(root):
    if not root:
        return -1
    return 1 + max(height(root.left), height(root.right))


tree = BinarySearchTree()
t = int(input())

for _ in range(t):
    x = int(input())
    tree.create(x)

print(height(tree.root))
