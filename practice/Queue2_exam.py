class Queue:
    def __init__(self):
        self.list = []

    def enQueue(self,i):
        self.list.append(i)

    def deQueue(self):
        return self.list.pop(0)
    
    def peek(self):
        return self.list[0]
    
    def isEmpty(self):
        return self.list == []
    
    def size(self):
        return len(self.list)
    
q = Queue()
data = input("Enter Input : ").split(',')
for d in data:
    if d.startswith('EN'):
        _,num = d.split()
        q.enQueue(d)
        
    elif d == 'D':
        if not q.isEmpty():    
            num = q.deQueue()
            print(num.split()[1])
        else:
            print("Empty")
    elif d.startswith('ES'):
        insert = False
        for n in range(len(q.list)):
            if 'EN' in q.list[n]:
                q.list.insert(n,d)
                insert = True
        if not insert:
            q.enQueue(d)                