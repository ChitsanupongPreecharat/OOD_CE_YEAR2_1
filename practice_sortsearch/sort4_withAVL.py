class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = self.setHeight()
    
    def setHeight(self):
        a = self.getHeight(self.left)
        b = self.getHeight(self.right)
        self.height = max(a,b)+1
        return self.height
    
    def getHeight(self,node):
        return -1 if node is None else node.height
    
    def balanceValue(self):
        return self.getHeight(self.left) - self.getHeight(self.right)

class AVL:
    def __init__(self):
        self.root = None
    
    def add(self,word,method):
        self.root = self._add(word,self.root,method)
    
    def _add(self,word,root,method):
        if root is None:
            return Node(word)
        if method == 'W':
            data = sum(ord(ch)-96 for ch in word )
            cur_data = sum(ord(ch)-96 for ch in root.data)
            if data <= cur_data :
                root.left = self._add(word,root.left,method)
            else:
                root.right = self._add(word,root.right,method)
        
        if method == 'V':
            if self.compare(word,root.data) :
                root.left = self._add(word,root.left,method)
            else:
                root.right = self._add(word,root.right,method)

        root = self.rebalance(root)
        root.setHeight()
        return root
    
    def compare(self,word1,word2):
        priority = {'a':5,'e':4,'i':3,'o':2,'u':1}
        count1 = sum(1  for ch in word1 if ch in priority)
        count2 = sum(1  for ch in word2 if ch in priority)
        if count1 < count2:
            return True
        elif count1 > count2:
            return False
        else:
            max1 = max((priority[ch] for ch in word1 if ch in priority),default=0)
            max2 = max((priority[ch] for ch in word2 if ch in priority),default=0)
            return max1 > max2
    
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
            if x.right.balanceValue() > 0:
                x.right = self.rightRotate(x.right)
            x = self.leftRotate(x)
        elif balance > 1:
            if x.left.balanceValue() < 0:
                x.left = self.leftRotate(x.left)
            x = self.rightRotate(x)
        x.setHeight()
        return x
    
    def sort(self):
        self._sort(self.root)

    def _sort(self,root):
        if root is not None:
            self._sort(root.left)
            print(root.data,end=" ")
            self._sort(root.right)

avl = AVL()
animal, method = input("Enter Input : ").split('/')
animal = animal.split()
for a in animal:
    avl.add(a,method)
avl.sort()