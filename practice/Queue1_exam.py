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
i = 0
for d in data:
    if d.startswith('E'):
        _,num = d.split()
        q.enQueue(num)
        print(f"Add {num} index is {i}")
        i+=1
    elif d == 'D':
        if not q.isEmpty():
            num = q.deQueue()
            print(f"Pop {num} size in queue is {q.size()}")
            i-=1
        else:
            print("-1")
print(f"Number in Queue is :  {q.list} " if not q.isEmpty() else "Empty")