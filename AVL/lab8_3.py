class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = self.setHeight()
    
    def setHeight(self):
        a = self.getHeight(self.left)
        b = self.getHeight(self.right)
        self.height = 1 + max(a,b)
        return self.height
    
    def getHeight(self,node):
        return -1 if node is None else node.height
    
    def balanceValue(self):
        return self.getHeight(self.left) - self.getHeight(self.right)

class AVL:
    def __init__(self):
        self.root = None
    
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
        if balance < -1:
            if x.right.balanceValue()> 0:
                x.right = self.rightRotate(x.right)
            x = self.leftRotate(x)
        elif balance > 1:
            if x.left.balanceValue()<0:
                x.left = self.leftRotate(x.left)
            x = self.rightRotate(x)
        x.setHeight()
        return x
    
    def printTree(self,node,level=0):
        if node is not None:
            self.printTree(node.right,level+1)
            print('     '*level,node.data)
            self.printTree(node.left,level+1)
    
    def maxsum(self, node):
        if node is None:
            return (0, [])  

        if node.left is None and node.right is None:  
            return (node.data, [node.data])

        left_sum, left_path = self.maxsum(node.left)
        right_sum, right_path = self.maxsum(node.right)

        if left_sum > right_sum:
            return (node.data + left_sum, [node.data] + left_path)
        else:
            return (node.data + right_sum, [node.data] + right_path)


avl = AVL()
Input = list(map(int,input("Enter tree nodes: ").split()))
for i in Input:
    avl.add(i)
avl.printTree(avl.root)
total,path = avl.maxsum(avl.root)
print()
print(f"Path with maximum sum: {' + '.join( str(i) for i in path)} = {str(total)}")