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


git = input("Git History: ").split('|')

tail_num = []
for g in git:
    l = LinkedList()
    nums = g.split("->")
    for n in nums:
        l.append(n)
    tail_num.append(int(l.peek_tail()))

for t in range(len(tail_num)-1):
    if tail_num[t] != tail_num[t+1]:
        same_repository = False
        break
    else:
        same_repository = True
print(tail_num)
print(same_repository)
