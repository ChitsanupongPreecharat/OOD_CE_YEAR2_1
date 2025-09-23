class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self,data):
        data = Node(data)
        if self.head is None:
            self.head = data
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = data
        self.size += 1

    def print_list(self):
        result = ''
        p = self.head
        while p:
            result  += str(p.data)
            if p.next:
                result += '->'
            p = p.next
        return result
    
    def sort(self):
        # swap = True
        # while swap :
        #     swap = False
        #     prev = None
        #     current =  self.head
        #     while current.next:
        #         nxt = current.next
        #         if current.data > current.next.data:
        #             swap = True
        #             if prev is None:
        #                 self.head = nxt
        #             else:
        #                 prev.next = nxt
                    
        #             current.next = nxt.next
        #             nxt.next = current
        #             prev = nxt
        #         else:
        #             prev = current
        #             current = current.next

        swap = True
        while swap:
            swap = False
            prev = None
            current = self.head
            while current.next:
                nxt = current.next
                if current.data > current.next.data:
                    swap = True
                    if prev is None:
                        self.head = nxt
                    else:
                        prev.next = nxt
                    
                    current.next = nxt.next
                    nxt.next = current
                    prev = nxt
                else:
                    prev = current
                    current = current.next

L = LinkList()
Input = list(map(int,input("Enter Input: ").split(',')))
for i in Input:
    L.append(i)
print(f"Input List: {L.print_list()}")
print("_______________________________________")
L.sort()
print("_______________________________________")
print(f"Sorted List: {L.print_list()}")