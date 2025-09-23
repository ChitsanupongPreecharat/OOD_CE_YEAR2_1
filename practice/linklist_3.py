class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        p = Node(data)
        if self.head is None:
            self.head = p
        else:
            q = self.head
            while q.next:
                q = q.next
            q.next = p
    
    def print_list(self):
        result = ''
        if self.head is None : return 
        p = self.head
        while p:
            result += p.data
            if p.next :
                result += ' -> '
            p = p.next
        return result
    
    def peek_tail(self):
        if self.head is None: return 
        p = self.head
        while p.next:
            p = p.next
        return p.data


Input = input("Git History: ").split('|')
branches = []
for n in Input:
    L = LinkList()
    n = list(n.split('->'))
    for i in n:
        L.append(i.strip())
    branches.append(L)

def same_repo(branches):
    prev_tail = None
    for b in branches:
        tail = b.peek_tail()
        
        if prev_tail is None:
            prev_tail = tail
        if prev_tail != tail:
            return False
    return True


def merge(branches):
    merge_count = 0
    temp = 0
    for i in range(len(branches)):
        for j in range(i+1,len(branches)):
            a = branches[i].head
            b = branches[j].head
            while a:
                while b:
                    if a.data == b.data:
                        temp +=1
                        
                    b = b.next
                a = a.next
            if temp >= 2:
                merge_count += 1
            temp = 0
    return merge_count



    














if same_repo(branches):
    print("Are these branches in the same repository? True")
    print(f"{merge(branches)} Merge(s)")
else:
    print("Are these branches in the same repository? False")


