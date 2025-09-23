class Stack:
    def __init__(self):
        self.list = []

    def push(self,i):
        self.list.append(i)

    def pop(self):
        if not self.is_emtpy():
            return self.list.pop(-1)
    
    def peek(self):
        if not self.is_emtpy():
            return self.list[-1]
    
    def is_emtpy(self):
        return len(self.list) == 0
    
    def size(self):
        return len(self.list)
    
    def __str__(self):
        result = ''
        for i in self.list:
            result += str(i)
            result += ' '
        return result
        
print("***Always 5 or 10***")
num = list(map(int,input("Enter Input : ").split()))
s = Stack()
for n in num:
    m = s.peek()
    if s.is_emtpy():
        s.push(n)
        continue
    elif n+m == 5 or m-n == 5 or n+m == 10 or m-n == 10:
        s.push(n)

print(f"Output : {s}")
