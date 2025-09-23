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
        if root is not None:
            self._inorder(root.left)
            print(root.data, end=" ")
            self._inorder(root.right)
    def kth_smallest(self, k):
        result = []
        self._inorder_list(self.root, result)
        if 1 <= k <= len(result):
            return result[k-1]
        return None

    def _inorder_list(self, root, result):
        if root:
            self._inorder_list(root.left, result)
            result.append(root.data)
            self._inorder_list(root.right, result)

avl = AVL()
print("*** Simple but more ***")
n,data,k = input("input  N node, Data, K small : ").split(',')
n = int(n)
data = list(map(int,data.split()))
k = int(k)
for i in range(n):
    avl.add(data[i])

print(avl.kth_smallest(k))