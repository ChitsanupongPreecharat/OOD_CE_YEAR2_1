class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

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

    def __str__(self):
        result = ''
        p = self.head
        while p:
            result += str(p.data)
            result += ' '
            p = p.next
        return result
L = LinkList()
num = list(map(int,input("Enter Input : ").split()))
number = ' '.join(str(i) for i in num if i is not None)
print(f"Linked list now is {number}")
temp = []
remove =0
for n in num:
    if n not in temp:
        L.append(n)
        temp.append(n)
    else:
        remove += 1
print(f"there are {remove} duplicates that been remove")
print(f"Remove duplicates Linked list {L}")
