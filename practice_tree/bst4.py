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
    
    def search(self,root,path,treasure,escape,found_treasure=False,found_escape=False):
        if root is None:
            return False,found_treasure,found_escape
        
        path.append(root.data)

        if root.data == treasure and not found_treasure:
            print("Found Treasure !!!")
            found_treasure = True
        
        if root.data == escape and not found_escape and found_treasure:
            print("Found Escape !!!")
            found_escape = True
        
        print(("✅"if found_escape and found_treasure else "❌")," -> ".join(map(str,path)))

        if found_treasure and found_escape:
            return True,found_treasure,found_escape
        
        done,found_treasure,found_escape = self.search(root.left,path[:],treasure,escape,found_treasure,found_escape)
        if done:
            return True,found_treasure,found_escape
        
        done, found_treasure, found_escape = self.search(root.right, path[:], treasure, escape, found_treasure, found_escape)
        if done:
            return True, found_treasure, found_escape   
        
        return False,found_treasure,found_escape

T = BST()
num,treasure,escape = input("Enter Input : ").split('/')
num = list(map(int,num.split()))
treasure = int(treasure)
escape = int(escape)

for n in num:
    T.inorder(n)
T.printTree(T.root)
print("-------------------------------------------------")
done,found_treasure,found_escape = T.search(T.root,[],treasure,escape)
if done and found_treasure and found_escape:
    print(">>> Mission Complete <<<")
else:
    print(">>> Mission Failed <<<")