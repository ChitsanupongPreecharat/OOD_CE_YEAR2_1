class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.size += 1
            return
        
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = new_node
        self.size +=1

    def print_list(self):
        result = ''
        current = self.head
        while current:
            result += current.data
            if current.next is not None:
                result += ' → '
            current = current.next
        return result
    
    def operation(self,target):
        # if self.head is None or target <= 0: return
        # prev_i = None
        # i = self.head
        # while i:
        #     prev_j = i
        #     j = i
        #     for _ in range(target-1):
        #         if j.next is None :
        #             break
        #         prev_j = j
        #         j = j.next
            
        #     if prev_i:
        #         prev_i.next = j
        #     else:
        #         self.head = j
            
        #     if prev_j != i:
        #         prev_j.next = i
        #     if i.next == j:
        #         i.next = j.next
        #         j.next = i
        #     else:
        #         i.next,j.next = j.next,i.next
            
            
        #     prev_i = i
        #     i = i.next
        #     for _ in range(target):
        #         if i is None:
        #             break
        #         prev_i = i
        #         i = i.next


        if self.head is None or target<=0:return
        prev_i = None
        i = self.head
        while i:
            prev_j = i
            j = i
            for _ in range(target-1):
                if j is None:
                    break
                prev_j = j
                j = j.next
            
            if prev_i:
                prev_i.next = j
            else:
                self.head = j
            
            if prev_j != i:
                prev_j.next = i
            
            if i.next == j:
                i.next = j.next
                j.next = i
            else:
                i.next,j.next = j.next,i.next

            prev_i = i
            i = i.next
            for _ in range(target):
                if i is None:
                    break
                prev_i = i
                i = i.next
            
        

print(" *** Ant Army ***")
L = LinkedList()
num,target = input("Input : ").split(',')
num = list(num.split())
target = int(target)
for n in num:
    L.append(n)
print(f"Before : {L.print_list()}")
L.operation(target)
print(f"After : {L.print_list()}")

