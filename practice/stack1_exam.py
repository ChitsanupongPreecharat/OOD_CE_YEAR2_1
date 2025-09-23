class Stack:
    def __init__(self):
        self.list = []
    
    def push(self,data):
        self.list.append(data)

    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[-1]
    
    def isEmpty(self):
        return len(self.list) == 0
    
    def size(self):
        return len(self.list)
    
data = list(map(str,input("input: ")))
s = Stack()
def check(i,j):
    left = ['(','{','[']
    right = [')','}',']']
    return left.index(i) == right.index(j)

def baland(data):
    for d in data:
        if d in '({[':
            s.push(d)
        elif d in')}]':
            if s.isEmpty():
                return "Invalid"
            elif not check(s.peek(),d):
                return "Invalid"
            s.pop()
        else:
            return "Invalid"
    return "Valid" if s.isEmpty() else "Invalid"
print(baland(data))