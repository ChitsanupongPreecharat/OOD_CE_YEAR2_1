
class Queue:
    def __init__(self):
        self.item = []
    def enQueue(self,i):
        self.item.append(i)
    def deQueue(self):
        return self.item.pop(0)
    def is_Empty(self):
        return len(self.item) == 0
    def size(self):
        return len(self.item)
    def get_item(self):
        return list(self.item)    

Input = input("Enter Input : ").split(',')
q = Queue()
i = 0
for command in Input:
    method_value = command.strip()
    if method_value.startswith('E'):
        _,value = method_value.split()
        q.enQueue(value)
        print(f"Add {value} index is {i}")
        i += 1
    elif method_value.startswith('D'):
        if q.size() > 0:
            value = q.deQueue()
            print(f"Pop {value} size in queue is {q.size()} ") 
            i -= 1 
        else:
            print("-1") 

if not q.is_Empty():
    print(f"Number in Queue is :  {q.get_item()}")  
else: 
    print("Empty")            
