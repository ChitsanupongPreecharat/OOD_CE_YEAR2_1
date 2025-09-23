class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = self.setHeight()

    def setHeight(self):
        a = self.getHeight(self.left)
        b = self.getHeight(self.right)
        self.height = 1 + max(a, b)
        return self.height

    def getHeight(self, node):
        return -1 if node is None else node.height

    def balanceValue(self):
        return self.getHeight(self.left) - self.getHeight(self.right)


class AVL:
    def __init__(self):
        self.root = None

    def add(self, word,mode):
        self.root = self._add(self.root, word,mode)
    
    def compare(self,word1,word2):
        priority = {'a':5,'e':4,'i':3,'o':2,'u':1}
        count1 = 0
        count2 = 0
        for w1 in word1:
            if w1 in priority:
                count1 += 1
        for w2 in word2:
            if w2 in priority:
                count2 +=1
        if count1 < count2 :
            return True
        elif count1 > count2:
            return False
        else:
            max1 = max((priority[ch] for ch in word1.lower() if ch in priority),default=0)
            max2 = max((priority[ch] for ch in word2.lower() if ch in priority),default=0)
            return max1 > max2


    def _add(self, root, word,mode):
        if root is None:
            return Node(word)
        if mode == 'W':
            data = sum(ord(ch.lower())-ord('a') + 1 for ch in word)
            cur_data = sum(ord(ch.lower())-ord('a') + 1 for ch in root.data)
            
            if data <= cur_data:
                root.left = self._add(root.left, word,mode)
            else:
                root.right = self._add(root.right, word,mode)
        if mode == 'V':
            
            if self.compare(word,root.data):
                root.left = self._add(root.left, word,mode)
            else:
                root.right = self._add(root.right, word,mode)
        
        

        root = self.rebalance(root)
        root.setHeight()
        return root

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        x.setHeight()
        y.setHeight()
        return y

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        x.setHeight()
        y.setHeight()
        return y

    def rebalance(self, x):
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

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, root):
        if root is not None:
            self._inorder(root.left)
            print(root.data, end=" ")
            self._inorder(root.right)

T = AVL()
print("***Fun with Word***")
word , mode = input("Enter Input : ").split('/')
word = list(word.split())
for w in word:
    T.add(w,mode)
T.inorder()