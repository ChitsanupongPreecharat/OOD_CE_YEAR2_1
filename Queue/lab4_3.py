class Queue:
    def __init__(self):
        self.items = []

    def enQueue(self, value):
        self.items.append(value)

    def deQueue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return None
    
    def peek(self):
        return self.items[0]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    
q = Queue()
code,hint = input("Enter code,hint : ").split(',')
ord_num = ord(code[0]) - ord(hint)
for i in code :
    q.enQueue(chr(ord(i)-ord_num))
    print(q.items)
    