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
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self.printTree(node.left, level + 1)

    def sum_tree(self,root):
        if root is None:
            return 0
        return root.data + self.sum_tree(root.left) + self.sum_tree(root.right)
    
    def muti_tree(self,root,target):
        target = int(target)
        if root:
            if root.data > target:
                root.data = root.data*target
            self.muti_tree(root.left,target)
            self.muti_tree(root.right,target)


T = BST()
print("**Sum of tree**")
num , target = input("Enter input : ").split("/")
num = list(num.strip().split())
temp = []
for n in num:
    if n not in temp:
        T.add(n)
        temp.append(n)
print()
print("Tree before:")
T.printTree(T.root)
print(f"Sum of all nodes = {T.sum_tree(T.root)}")

T.muti_tree(T.root,target)
print()
print("Tree after:")
T.printTree(T.root)
print(f"Sum of all nodes = {T.sum_tree(T.root)}")