class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        self.root = self._insert(self.root,data)

    def _insert(self,root,data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self._insert(root.left,data)
        else:
            root.right = self._insert(root.right,data)
        return root
    
    def travel(self,root,l):
        if root is None:
            l = []
        if root:
            self.travel(root.left,l)
            l.append(root.data)
            self.travel(root.right,l)
        return l
    
    def fine_path_sum(self,root,target):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.data == target
        target -= root.data
        return self.fine_path_sum(root.left,target) or self.fine_path_sum(root.right,target)
    
T = BST()
num,target = input("Enter the values to insert into BST and target sum : ").split('/')
num = list(map(int,num.split()))
for n in num:
    T.insert(n)
print(f"Inorder Traversal of BST : {' '.join(str(t) for t in T.travel(T.root,[]))}")
print(f'Path with sum 10 exists : {T.fine_path_sum(T.root,int(target))}')
        
        