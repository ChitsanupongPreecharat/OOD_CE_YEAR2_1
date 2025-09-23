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
    
    def printL(self):
        result = ''
        q = self.head
        while q:
            result += str(q.data)
            if q.next:
                result += '->'
            q = q.next

        return result 
    
    def bubbleSort(self):
        if not self.head: return 
        swap = True
        while swap:
            cur = self.head
            swap = False
            while cur and cur.next:
                if cur.data > cur.next.data:
                    print()
                    print(f"Swapping {cur.data} and {cur.next.data}")
                    cur.data,cur.next.data = cur.next.data,cur.data
                    print(f"List: {self.printL()}")
                    swap = True
                cur = cur.next
    
L = LinkList()
print("*****Bubble Sort Linked List*****")
num = list(map(int,input("Enter Input: ").split(',')))
for n in num:
    L.append(n)
print(f"Input List: {L.printL()}")
print("_______________________________________")

L.bubbleSort()

print("_______________________________________")
print(f"Sorted List: {L.printL()}")