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
