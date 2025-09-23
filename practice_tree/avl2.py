class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = self.setHeight()
    
    def setHeight(self):
        a = self.getHeight(self.left)
        b = self.getHeight(self.right)
        self.height = 1 + max(a,b)
        return self.height
    
    def getHeight(self,node):
        return -1 if node == None else node.height
    
    def balanceValue(self):
        return int(self.getHeight(self.left)) - int(self.getHeight(self.right))

class AVL:
    def __init__(self):
        self.root = None
    
    def leftRotate(self,x):
        y = x.right
        x.right = y.left
        y.left = x
        x.setHeight()
        y.setHeight()
        return y
    
    def rightRotate(self,x):
        y = x.left
        x.left = y.right
        y.right = x
        x.setHeight()
        y.setHeight()
        return y
    
    def rebalance(self,x):
        if x is None:
            return x
        
        balance = x.balanceValue()

        if balance < -1 :
            if x.right.balanceValue() > 0:
                x.right= self.rightRotate(x.right)
            x = self.leftRotate(x)

        if balance > 1 :
            if x.left.balanceValue() < 0:
                x.left = self.leftRotate(x.left)
            x  = self.rightRotate(x)
        
        x.setHeight()
        return x
    
    def add(self,data):
        self.root = self._add(self.root,data)

    def _add(self,root,data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self._add(root.left,data)
        else:
            root.right = self._add(root.right,data)
        
        root = self.rebalance(root)
        root.setHeight()
        return root
    
    def printTree(self,root,level=0):
        if root :
            self.printTree(root.right,level+1)
            print('    '*level,str(root.data))
            self.printTree(root.left,level+1)

def same_tree(t1,t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    if t1.data != t2.data:
        return False
    return same_tree(t1.left,t2.left) and same_tree(t1.right,t2.right)

tree1 = AVL()
tree2 = AVL()
t1,t2 = input("Enter Tree1/Tree2 : ").split('/')
t1 = list(map(int,t1.split()))
t2 = list(map(int,t2.split()))

for t in t1:
    tree1.add(t)
for t in t2:
    tree2.add(t)      

print("Tree 1")
tree1.printTree(tree1.root)
print()
print("Tree 2")
tree2.printTree(tree2.root)
print()
if same_tree(tree1.root,tree2.root):
    print("Same Tree")
else:
    print("Different Tree")