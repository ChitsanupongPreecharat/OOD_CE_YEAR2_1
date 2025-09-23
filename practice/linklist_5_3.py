class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = new_node

    def print_list(self):
        result = ''
        current = self.head
        while current:
            result += str(current.data)
            if current.next:
                result += ' → '
            current = current.next
        return result
    
    def operation(self,num):
        # if self.head is None or num <= 0 : return
        # prev_i = None
        # i = self.head
        # while i:
        #     prev_j = i
        #     j = i
        #     for _ in range(num-1):
        #         if j is None:
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
        #     for _ in range(num):
        #         if i is None:
        #             break
        #         prev_i = i
        #         i = i.next

        if self.head is None or num <= 0 : return 
        prev_i = None
        i = self.head
        while i:
            prev_j = i
            j = i
            for _ in range(num-1):
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

            for _ in range(num):
                if i is None:
                    break
                prev_i = i
                i = i.next


print(" *** Ant Army ***")
L = LinkedList()
l ,num = input("Input : ").split(',')
l = list(map(int,l.split()))
num = int(num)
for i in l:
    L.append(i)
print(f"Before : {L.print_list()}")
L.operation(num)
print(f"After : {L.print_list()}")