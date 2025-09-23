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
        if x == None:
            return x

        balance = x.balanceValue()    

        if balance < -1:
            if x.right.balanceValue() > 0:
                x.right = self.rightRotate(x.right)
            x = self.leftRotate(x)
        
        if balance > 1:
            if x.left.balanceValue() < 0:
                x.left = self.leftRotate(x.left)
            x = self.rightRotate(x)
        
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

        root =self.rebalance(root)
        root.setHeight()
        return root
    
    def printTree(self,root,level=0):
        if root:
            self.printTree(root.right,level+1)
            print('     ' * level , root.data)
            self.printTree(root.left,level+1)

    def max_sum(self,root,result):
        if root:
            result.append(root.data)
            if root.right:
                self.max_sum(root.right,result)
            else:
                self.max_sum(root.left,result)
        return result

T = AVL()
num = list(map(int,input("Enter tree nodes: ").split()))
for n in num:
    T.add(n)
T.printTree(T.root)
result = T.max_sum(T.root,[])
maxsum = sum(result)
print(f"Path with maximum sum: {' + '.join(str(n) for n in result)} = {maxsum}")