class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    
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
        return root
    
    def printTree(self, root, level=0):
        if root is not None:
            self.printTree(root.right, level + 1)
            print('     ' * level, root.data)
            self.printTree(root.left, level + 1)
    
    def find_paths_to_leaves(self):
        result = []
        self._dfs_to_leaves(self.root, [], result)
        return result

    def _dfs_to_leaves(self, node, path, result):
        if not node:
            return
        path.append(node.data)
        if not node.left and not node.right:  
            result.append(list(path))
        else:
            self._dfs_to_leaves(node.left, path, result)
            self._dfs_to_leaves(node.right, path, result)
        path.pop()
    
    def delete_path(self, path):
        if not path:
            return
        current = self.root
        parent = None
        for i, data in enumerate(path):
            if not current:
                return
            if current.data != data:
                return
            if i == len(path) - 1:  # reached the last node in the path
                if not parent:
                    self.root = None
                elif parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
                return
            parent = current
            if current.left and current.left.data == path[i + 1]:
                current = current.left
            elif current.right and current.right.data == path[i + 1]:
                current = current.right
            else:
                return

# ----- MAIN -----
user_input = input("Enter <Create City A (BST)>/<Create conditions and deploy the army>: ")
num_str, actions_str = user_input.split("/")
num = list(map(int, num_str.split()))
conditions = [c.strip().split() for c in actions_str.split(',')]

tree = BST()
for n in num:
    tree.add(n)

print("(City A) Before the war:")
tree.printTree(tree.root)

battle_ongoing = True
for c in conditions:
    if not battle_ongoing:
        break
    
    cond, k_str = c
    k = int(k_str)

    if cond == 'L':
        text = 'less than'
    elif cond == 'M':
        text = 'greater than'
    else:
        text = 'equal to'
    print("--------------------------------------------------")
    print(f"Removing paths where the sum is {text} {k}:")

    city_destroyed_count = 0
    while True:
        paths = tree.find_paths_to_leaves()
        matched = []
        for p in paths:
            s = sum(p)
            if (cond == "L" and s < k) or \
            (cond == "M" and s > k) or \
            (cond == "EQ" and s == k):
                matched.append((p, s))

        if not matched:
            break 

        # sort matched: path ที่ลึกกว่าอยู่ก่อน
        matched.sort(key=lambda x: -len(x[0]))

        for p, s in matched:
            city_destroyed_count += 1
            print(f"{city_destroyed_count}) {'->'.join(map(str, p))} = {s}")
            tree.delete_path(p)

            if not tree.root:
                battle_ongoing = False
                break

        if not battle_ongoing:
            break

    
    if city_destroyed_count == 0:
        print("No paths were removed.")

    if battle_ongoing:
        print("--------------------------------------------------")
        print("(City A) After the war:")
        tree.printTree(tree.root)
        
if not battle_ongoing:
    print("--------------------------------------------------")
    print("(City A) After the war:")
    print("City A has fallen!")
