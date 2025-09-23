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

    def printList(self):
        result = []
        t = self.head
        while t is not None:
            result.append(str(t.data))
            t = t.next
        return ' → '.join(result)
    
    def swap_army(self,num):
        cur = self.head
        index = 0
        if num == 0:
            cur = None
            
        while cur:
            group_cur = []
            temp = cur
            for _ in range(num):
                if temp:
                    group_cur.append(temp)
                    temp = temp.next
                else:
                    break
            
            if len(group_cur) <= num and index % 2 == 0:
                i = 0
                j = min(num,len(group_cur)-1)
                while i < j:
                    group_cur[i].data,group_cur[j].data = group_cur[j].data,group_cur[i].data
                    i += 1
                    j -= 1
            cur = temp
            index += 1
                    
        print(f"After : {self.printList()}")

           
l = LinkedList()
print(" *** Ant Army ***")
ants,num = input("Input : ").split(',')
ants = list(map(int,ants.split()))
for an in ants:
    l.append(an)
print(f"Before : {l.printList()}")
l.swap_army(int(num))

            
