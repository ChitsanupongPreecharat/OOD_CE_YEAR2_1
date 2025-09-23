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

    def add(self, data):
        self.root = self._add(self.root, data)

    def _add(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self._add(root.left, data)
        else:
            root.right = self._add(root.right, data)

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

        # Right heavy
        if balance < -1:
            if x.right.balanceValue() > 0:  # RL case
                x.right = self.rightRotate(x.right)
            x = self.leftRotate(x)

        # Left heavy
        elif balance > 1:
            if x.left.balanceValue() < 0:  # LR case
                x.left = self.leftRotate(x.left)
            x = self.rightRotate(x)

        x.setHeight()
        return x

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, root):
        result = []
        if root is not None:
            self._inorder(root.left)
            result.append(root.data)
            self._inorder(root.right)
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('    ' * level+str(node.data))
            self.printTree(node.left, level + 1)
def check_same_tree(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    if tree1.data != tree2.data:
        return False
    return (check_same_tree(tree1.left, tree2.left) and
            check_same_tree(tree1.right, tree2.right))


avl1 = AVL()
avl2 = AVL()
tree1,tree2 = input("Enter Tree1/Tree2 : ").split('/')
tree1 = list(map(int,tree1.strip().split()))
tree2 = list(map(int,tree2.strip().split()))
for i in tree1:
    avl1.add(i)
for j in tree2:
    avl2.add(j)
print("Tree 1")
avl1.printTree(avl1.root)
print()
print("Tree 2")
avl2.printTree(avl2.root)
print()
if check_same_tree(avl1.root, avl2.root):

    print("Same Tree")

else:

    print("Different Tree")