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
        data = int(data)
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self._add(root.left,data)
        else:
            root.right = self._add(root.right,data)
        return root
    def printTree(self, root, l=None):
        if l is None:
            l = []
        if root:
            self.printTree(root.left, l)   
            l.append(root.data)            
            self.printTree(root.right, l)  
        return l

    def fine(self,root,target):
        if self.sum(root) == target:
            return True
        else:
            return self.path(root,target)
    def sum(self,root):
        if root is None:
            return 0
        return int(root.data) + self.sum(root.left) + self.sum(root.right)

    def path(self,root,target):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.data == target
        target -= int(root.data)
        return self.path(root.left,target) or self.path(root.right,target)
        
        
        
    
T=BST()

num,target = input("Enter the values to insert into BST and target sum : ").split('/')
num = list(num.strip().split())
target = int(target)
for n in num:
    T.add(n)

tree = T.printTree(T.root)
all_tree = ' '.join(map(str,tree))
print(f"Inorder Traversal of BST : {all_tree}")

print(f"Path with sum {target} exists : {T.fine(T.root,target)}")