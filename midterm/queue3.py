class Queue:
    def __init__(self):
        self.item = []
    
    def enQueue(self,i):
        self.item.append(i)
    
    def deQueue(self):
        if not self.is_empty():
            return self.item.pop(0)
        
    def peek(self):
        if not self.is_empty():
            return self.item[0]
    
    def is_empty(self):
        return len(self.item) == 0
    
    def size(self):
        return len(self.item)
    
q = Queue()
code,hint = input("Enter code,hint : ").split(',')
encode = ord(code[0])-ord(hint)
for c in code:
    q.enQueue(chr(ord(c)-encode))
    print(q.item)