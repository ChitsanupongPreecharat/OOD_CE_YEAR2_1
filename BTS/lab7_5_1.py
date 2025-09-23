class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
class BST:
    def __init__(self):
        self.root = None
    
    def add(self,data):
        self.root= self._add(self.root,data)

    def _add(self,root,data):
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = self._add(root.left,data)
        else:
            root.right = self._add(root.right,data)    
        return root
    def printTree(self,root,level=0):
        if root is not None:
            self.printTree(root.right,level+1)
            print('     ' * level, root.data)
            self.printTree(root.left,level+1)
        
    def find_path(self):
        result = []
        self.fp(self.root,[],result)
        return result
    
    def fp(self,root,path,result):
        if not root:return
        
        path.append(root.data)
        if not root.left and not root.right:
            result.append(list(path))
        if root.left:
            self.fp(root.left,path,result)
        if root.right:
            self.fp(root.right,path,result)
        path.pop()

    def delete(self, root, key):
        if not root:
            return root

        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            
            if not root.left and not root.right:
                return None
           
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            succ = self._min_value(root.right)
            root.data = succ.data
            root.right = self.delete(root.right, succ.data)

        return root

    def _min_value(self, node):
        while node.left:
            node = node.left
        return node


T = BST()
Input,actions = input("Enter <Create City A (BST)>/<Create conditions and deploy the army>: ").split('/')
Input = list(map(int,Input.split()))
actions = actions.split(',')
for i in Input:
    T.add(i)

print("(City A) Before the war:")
T.printTree(T.root)
for ac in actions:
    cond , k = ac.split()
    k = int(k)
    if cond == 'L':
        text = 'less than'
    elif cond == 'M':
        text = 'greater than'
    else:
        text = 'equal to'

    print("--------------------------------------------------")
    print(f"Removing paths where the sum is {text} {k}:")

    count = 0
    while True:
        found = False
        path = T.find_path()   
        match = []
        for p in path:
            s = sum(p)
            if cond == 'L' and s < k:
                match.append((p,s))
            elif cond == 'EQ' and s == k :
                match.append((p,s))
            elif cond == 'M' and s > k:
                match.append((p,s))

        if not match:   
            break

        
        for p,s in match:
            count += 1
            print(f"{count}) {'->'.join(map(str,p))} = {s}")
            T.delete(T.root, p[-1])   
            found = True
        
        if not found:
            break

    if count == 0:
        print("No paths were removed.")
    print("--------------------------------------------------")
    print("(City A) After the war:")
    T.printTree(T.root)


