class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def add(self,data):
        self.root = self.add_(self.root,data)
    
    def add_(self,root,data):
        
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.add_(root.left,data)
        else:
            root.right = self.add_(root.right,data)
        return root
    
    def printTree(self,root,level = 0):
        if root is not None:
            self.printTree(root.right,level+1)
            print('     ' * level, root.data)
            self.printTree(root.left,level+1)
    
    def search(self, root, path, treasure, escape, found_treasure=False, found_escape=False):
        if root is None:
            return False, found_treasure, found_escape  

        path.append(root.data)

        if root.data == treasure and not found_treasure:
            print("Found Treasure !!!")
            found_treasure = True

        
        if root.data == escape and not found_escape and found_treasure:
            print("Found Escape !!!")
            found_escape = True
        
        print(("✅" if found_treasure and found_escape else "❌"), " -> ".join(map(str, path)))

        

        
        if found_treasure and found_escape:
            
            return True, found_treasure, found_escape   

        
        done, found_treasure, found_escape = self.search(root.left, path[:], treasure, escape, found_treasure, found_escape)
        if done:
            return True, found_treasure, found_escape   

        
        done, found_treasure, found_escape = self.search(root.right, path[:], treasure, escape, found_treasure, found_escape)
        if done:
            return True, found_treasure, found_escape   

        return False, found_treasure, found_escape



                    

T = BST()
space,treasure,escape = input("Enter Input : ").split("/")
space = list(map(int,space.split()))
treasure = int(treasure)
escape = int(escape)
for n in space:
    T.add(n)
T.printTree(T.root)
print("-------------------------------------------------")
done, found_treasure, found_escape = T.search(T.root,[],treasure,escape)
if done and found_treasure and found_escape:
    print(">>> Mission Complete <<<")
else:
    print(">>> Mission Failed <<<")