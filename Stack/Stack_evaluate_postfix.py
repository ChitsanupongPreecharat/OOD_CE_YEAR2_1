class Stack:
    def __init__(self,list=None):
        if list == None:
            self.item = []
        else:
            self.item = list
    
    def push(self,i):
        self.item.append(i)
    def pop(self):
        if not self.isEmpty():
            return self.item.pop()
    def peek(self):
        return self.item[-1]
    def isEmpty(self):
        return self.item == []
    def size(self):
        return len(self.item)      

def evaluate_postfix(expression):
    
    for token in expression:
        if token.isdigit():
            s.push(int(token))
        elif token in '+-*/':    
            b = s.pop()
            a = s.pop()
            if token == '+':
                s.push(a+b)
            elif token == '-':
                s.push(a-b)
            elif token == '*':
                s.push(a*b)
            elif token == '/':
                s.push(a/b)
        else:
            print(f"Unknown oprator : {token}")   
    return s.pop()


s = Stack()
expr = '6523+8*-3+*'
result = evaluate_postfix(expr)
print(result)



