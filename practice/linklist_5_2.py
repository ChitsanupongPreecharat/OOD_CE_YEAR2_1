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
    
    def __str__(self):
        result = []
        cur = self.head
        while cur:
            result.append(str(cur.data))
            cur = cur.next
        return '->'.join(result)

    def bubbleSort(self):
        
        swap = True
        while swap:
            swap = False
            cur = self.head
            while cur and cur.next:
                if cur.data > cur.next.data:
                    print(f"Swapping {cur.data} and {cur.next.data}")
                    cur.data , cur.next.data = cur.next.data,cur.data
                    swap = True
                    print(f"List: {l}")
                cur = cur.next
l = LinkedList()
print("*****Bubble Sort Linked List*****")
num = list(map(int,input("Enter Input: ").strip().split(',')))
print(num)
for i in num:
    l.append(i)
print(f"Input List: {l}")
print("_______________________________________")
l.bubbleSort()
print("_______________________________________")
print(f"Sorted List: {l}")