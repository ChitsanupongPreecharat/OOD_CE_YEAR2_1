class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self,data):
        d = Node(data)
        if self.head is None:
            self.head = d
        else:
            h = self.head
            while h.next:
                h = h.next
            h.next = d
        self.size += 1
    
    def addHead(self,data):
        p = Node(data)
        p.next = self.head
        self.head = p 
        self.size += 1
    
    def removeHead(self):
        if self.head is None: return 
        if self.head.next is None:
            p = self.head
            self.head = None
        else:
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data
    
    def remvoeTail(self):
        if self.head is None : return
        if self.head.next is None :
            p = self.head
            self.head = None
        else:
            h = self.head
            while h.next.next:
                h = h.next
            h.next = h.next.next
        self.size -= 1
    
    def insertAfter(self,i,data):
        p = Node(data)
        q = self.head
        count = 0
        while q is not None:
            if count == i:
                p.next = q.next
                q.next = p
                return 
            q = q.next
            count += 1
        
    def deleteAfter(self,i):
        q = self.head
        count = 0
        while q is not None:
            if count == i:
                q.next = q.next.next
                self.size -= 1
                return 
            q = q.next
            count +=1
    
    def __str__(self):
        result = ''
        p = self.head
        while p:
            result += str(p.data)
            if p.next:
                result += ' -> '
            p = p.next
        return result

L = LinkList()
L.append(15)
L.append(30)
L.addHead(48)
L.removeHead()
L.insertAfter(1,99)
L.deleteAfter(1)
print(L)
