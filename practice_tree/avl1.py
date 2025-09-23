class Node:
    def __init__(self ,data):
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
    
    def kth_smallest(self,k):
        result = self.inorder()
        return result[k-1]
        

    def inorder(self):
        result = []
        self._inorder(self.root,result)
        return result
    
    def _inorder(self,root,result):
        if root:
            self._inorder(root.left,result)
            result.append(root.data)
            self._inorder(root.right,result)

T = AVL()
print("*** Simple but more ***")
num,l,k = input("input  N node, Data, K small : ").split(',')
num = int(num)
l = list(map(int,l.split()))
k = int(k)

for n in range(num):
    T.add(l[n])
        
print(T.kth_smallest(k))        