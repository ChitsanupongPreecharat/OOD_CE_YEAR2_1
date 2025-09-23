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
    
    def insert(self,idx,value):
        self.items.insert(idx,value)


q = Queue()
inputs = input("Enter Input : ").split(',')
for i in inputs:
    if 'EN' in i:
        q.enQueue(i)
        continue
    elif 'ES' in i:
        insert = False
        for j in range(len(q.items)):
            if 'EN' in q.items[j]:
                q.insert(j,i)
                insert = True
                break
        if not insert:
            q.enQueue(i)    
    elif 'D' in i:
        number = q.deQueue()
        print(number.split()[1] if number is not None else "Empty")
        
        
        

  