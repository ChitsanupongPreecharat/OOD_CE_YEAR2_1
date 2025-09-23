class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def inorder(self,data):
        self.root = self._inorder(self.root,data)

    def _inorder(self,root,data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self._inorder(root.left,data)
        else:
            root.right = self._inorder(root.right,data)
        return root
    
    def printTree(self,root,level=0):
        if root:
            self.printTree(root.right,level+1)
            print('     '*level,root.data)
            self.printTree(root.left,level+1)
    
    def sum_tree(self,root):
        if root is None:
            return 0
        return root.data + self.sum_tree(root.left) + self.sum_tree(root.right)
    
    def muti(self,root,target):
        if root:
            if root.data > target:
                root.data = root.data * target
            self.muti(root.left,target)
            self.muti(root.right,target)

print("**Sum of tree**")
T = BST()
num , target = input("Enter input : ").split('/')
num = list(map(int,num.split()))
target = int(target)
temp = []

print("Tree before:")
for n in num:
    if n not in temp:
        T.inorder(n)
        temp.append(n)
T.printTree(T.root)
print(f'Sum of all nodes = {str(T.sum_tree(T.root))}')

print()
print("Tree after:")
T.muti(T.root,target)
T.printTree(T.root)
print(f'Sum of all nodes = {str(T.sum_tree(T.root))}')