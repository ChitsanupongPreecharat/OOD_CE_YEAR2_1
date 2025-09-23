class Queue:
    def __init__(self):
        self.item = []
    def enQueue(self,i):
        self.item.append(i)
    def deQueue(self):
        if not self.is_Empty():
            return self.item.pop(0)
        else:
            return None
    def is_Empty(self):
        return len(self.item) == 0
    def size(self):
        return len(self.item)                

q = Queue()
actions = input("Enter Input : ").split(',')
count = 0
for ac in actions:
    if ac.startswith('E'):
        _,num = ac.split()
        q.enQueue(num)
        print(f"Add {num} index is {count}")
        count += 1
    else:
        target = q.deQueue()
        print(f"Pop {target } size in queue is {q.size()}"if target is not None else '-1')
        if target is not None:
            count -= 1
print(f"Number in Queue is :  {q.item}"if not q.is_Empty() else "Empty")