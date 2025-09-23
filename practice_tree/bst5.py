class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
class BST:
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
        return root
    
    def printTree(self,root,level=0):
        if root:
            self.printTree(root.right,level+1)
            print('      ' * level , root.data)
            self.printTree(root.left,level+1)

    def delete_node(self, root, target):
        if not root:
            return root
        
        if root.data == target:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            succ = self.min_value(root.right)
            root.data = succ.data
            root.right = self.delete_node(root.right, succ.data)
            return root
        
        elif target < root.data:   # ✅ ต้องเช็คก่อนว่าควรลงซ้ายหรือขวา
            root.left = self.delete_node(root.left, target)
        else:
            root.right = self.delete_node(root.right, target)
        
        return root  # ✅ ต้องคืน root กลับเสมอ

    def min_value(self, node):
        while node.left:
            node = node.left
        return node


T = BST()
num = list(map(int,input("Enter Input : ").split()))

for n in num:
    T.add(n)
T.printTree(T.root)
T.delete_node(T.root,80)