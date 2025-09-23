class Stack:
    def __init__(self):
        self.item = []
    def pop(self):
        return self.item.pop() if not self.isEmpty() else None
    def peek(self):
        return self.item[-1] if not self.isEmpty() else None
    def push(self,i):
        self.item.append(i)
    def isEmpty(self):
        return len(self.item) == 0
    def size(self):
        return len(self.item)
    
print("***Always 5 or 10***")
number = list(map(int,input("Enter Input : ").split()))
s = Stack()
for i in number:
    if s.isEmpty():
        s.push(i)
    elif  s.peek() + i == 5 or s.peek() - i == 5 or s.peek() + i == 10 or s.peek() - i == 10:
        s.push(i)

result = ' '.join(map(str,s.item))        
print(f"Output : {result}")