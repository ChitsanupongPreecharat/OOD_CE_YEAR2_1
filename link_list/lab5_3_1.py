class Node:
        def __init__(self,data,next=None):
            self.data = data
            self.next = next
class LinkedList:
    

    def __init__(self):
        self.head = None
        self.size = 0

    def append(self,data):
        p = Node(data)
        if self.head is None:
             self.head = p
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = p
        self.size += 1
    
    def addHead(self,data):
        p = Node(data)
        p.next = self.head
        self.head = p
        self.size += 1

    def removeHead(self):
        if self.head == None:return
        if self.head.next == None:
            p = self.head
            self.head = None
        else:
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data

    def removeTail(self):
        if self.head == None : return
        if self.head.next == None:
            p = self.head
            self.head = None
            return p.data
        else:
            p = self.head
            while p.next.next != None:
                p = p.next
            p.next = p.next.next
            self.size -= 1
    def peek_tail(self):
        if self.head == None: return 
        if self.head.next ==None:
            return self.head.data
        else:
            p = self.head
            while p.next != None:
                p = p.next
            return p.data

    def insertAfter(self,i,data):
        p = Node(data)
        q = self.head
        count = 0
        while  q is not None:
            if count == i:
                p.next = q.next
                q.next = p 
                return
            q = q.next
            count += 1
        
    def deleteAfter(self,i):
        q = self.head
        count = 0
        while q != None and q.next != None:
            if count == i:
                p = q.next
                q.next = p.next
                p = None
                self.size -= 1
                return
            q = q.next
            count += 1

    def printList(self):
        result = []
        t = self.head
        while t is not None:
            result.append(str(t.data))
            t = t.next
        return ' '.join(result)
    
def build_all_branches(git_input):
    branches = []
    git = git_input.strip().split('|')
    for g in git:
        l = LinkedList()
        num = g.strip().split('->')
        for n in reversed(num):
            l.append(n.strip())
        branches.append(l)
    return branches

def same_repo(branches):
    head_num = []
    for i in range(len(branches)):
        head_num.append(branches[i].head.data)
    
    for j in range(len(head_num)-1):
        if head_num[j] != head_num[j+1]:
            return False
    return True

class Pair:
    def __init__(self,child,parent,next=None):
        self.child = child
        self.parnt = parent
        self.next = next

def count_merge(branches):
    pair_head = None
    for br in branches:
        cur = br.head
        while cur and cur.next:
            new_pair = Pair(cur.next.data,cur.data)
            new_pair.next = pair_head
            pair_head = new_pair
            cur = cur.next
    
    def is_in_list(head,data):
        cur = head
        while cur:
            if cur.data == data:
                return True
            cur = cur.next
        return False

    count = 0
    counted_children = None
    p = pair_head
    while p:
        child = p.child
        if is_in_list(counted_children,child):
            p = p.next
            continue

        parents_of_child = None
        cur_pair = pair_head
        while cur_pair:
            if cur_pair.child == child:
                if not is_in_list(parents_of_child,cur_pair.parnt):
                    parents_of_child = Node(cur_pair.parnt,parents_of_child)
            cur_pair = cur_pair.next      
    
        parent_count = 0
        temp = parents_of_child
        while temp:
            parent_count += 1
            temp = temp.next

        if parent_count > 1:
            count += 1
            counted_children = Node(child,counted_children)
    
        p = p.next
    return count

git = input("Git History: ")

branches = build_all_branches(git)

if same_repo(branches):
    print("Are these branches in the same repository? True")
    print(f"{count_merge(branches)} Merge(s)")
else:
    print("Are these branches in the same repository? False")