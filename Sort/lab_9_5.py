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

    def add(self, team):
        self.root = self._add(self.root, team)

    def _add(self, root, team):
        if root is None:
            return Node(team)
        if team.point < root.data.point:
            root.left = self._add(root.left, team)
        elif team.point > root.data.point:
            root.right = self._add(root.right, team)
        else:
            if team.gd < root.data.gd:
                root.left = self._add(root.left, team)
            else:
                root.right = self._add(root.right, team)

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
            self._inorder(root.right)
            print(root.data)
            self._inorder(root.left)

class Team:
    def __init__(self,name,win,loss,draw,scored,connected):
        self.name = name
        self.win = int(win)
        self.loss = int(loss)
        self.draw = int(draw)
        self.scored = int(scored)
        self.connected = int(connected)
        self.gd = self.scored - self.connected
        self.point = 3 * self.win + 1 * self.draw
    
    def __str__(self):
        return str([
            self.name,
            {'points': self.point},
            {'gd': self.gd}
        ])
T = AVL()
teams = input("Enter Input : ").split('/')
for t in teams:
    name, win, loss, draw, scored, connected = t.split(',')
    T.add(Team(name,win,loss,draw,scored,connected))
print("== results ==")
T.inorder()