class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.h = 1

        def update_height(self):
            pass
    
        def balance_factor(self):
            pass
        
    def __init__(self):
        self.root = None
    
    def insert(self,key):
        if not self.root:
            self.root = BST.Node(key)
        else:
            BST._insert(self.root,key)

    def _insert(node,key):
        if key < node.data:
            if node.left:
                BST._insert(node.left,key)
            else:
                node.left = BST.Node(key)
        else:
            if node.right:
                BST._insert(node.right,key)
            else:
                node.right = BST.Node(key)
   

    def _get_format(root,ans = ""):
        if root:
            temp = ""
            if root.right:
                temp += BST._get_format(root.right,ans + "     ")
            temp += f"{ans}{root.data}\n"
            if root.left:
                temp += BST._get_format(root.left,ans + "     ")
            return temp
        return ""
    
    def __str__(self):
        return BST._get_format(self.root)

################################
'''
⠀⠀⢘⣾⣾⣿⣾⣽⣯⣼⣿⣿⣴⣽⣿⣽⣭⣿⣿⣿⣿⣿⣧
⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⣰⣯⣾⣿⣿⡼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿
⠀⠀⠛⠛⠋⠁⣠⡼⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁
⠀⠀⠀⠤⣶⣾⣿⣿⣿⣦⡈⠉⠉⠉⠙⠻⣿⣿⣿⣿⣿⠿⠁⠀
⠀⠀⠀⠀⠈⠟⠻⢛⣿⣿⣿⣷⣶⣦⣄⠀⠸⣿⣿⣿⠗⠀⠀⠀
⠀⠀⠀⠀⠀⣼⠀⠄⣿⡿⠋⣉⠈⠙⢿⣿⣦⣿⠏⡠⠂⠀⠀⠀
⠀⠀⠀⠀⢰⡌⠀⢠⠏⠇⢸⡇⠐⠀⡄⣿⣿⣃⠈⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⣻⣿⢫⢻⡆⡀⠁⠀⢈⣾⣿⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⣻⣷⣾⣿⣿⣷⢾⣽⢭⣍⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⣿⣿⡿⠈⣹⣾⣿⡞⠐⠁⠀⠀⠀⠁⠀⠀⠀
⠀⠀⠀⠨⣟⣿⢟⣯⣶⣿⣆⣘⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡆⠀⠐⠶⠮⡹⣸⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

def isAVL(node : BST.Node):
    if node is None:
        return True,0
    left_ok,left_h = isAVL(node.left)
    right_ok,right_h = isAVL(node.right)
    balance = left_h-right_h
    ok = left_ok and right_ok and (-1<=balance<=1)
    height = 1 + max(left_h,right_h)
    return ok,height


################################


tree = BST()

print("**********IsAVL**********")
for i in list(map(int, input("Enter numbers to insert in the tree: ").split())):
    tree.insert(i)
print("Tree:")
print(tree)
result, _ = isAVL(tree.root)
print("Is AVL???:", result)