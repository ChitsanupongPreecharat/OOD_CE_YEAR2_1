class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        self.root = self._insert(self.root,data)

    def _insert(self,root,data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self._insert(root.left,data)
        else:
            root.right = self._insert(root.right,data)
        return root
    
    def printTree(self,node,level=0):
        if node != None:
            self.printTree(node.right,level+1)
            print('     ' * level, node.data)
            self.printTree(node.left,level+1)

T = BST()
num = list(map(int,input("Enter Input : ").split()))

for n in num:
    T.insert(n)
T.printTree(T.root)