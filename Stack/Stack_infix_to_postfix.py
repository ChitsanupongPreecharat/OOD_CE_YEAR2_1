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
    
def infix_to_postfix(expression):
    precedence ={
        '*':2,
        '/':2,
        '+':1,
        '-':1,
        '(':0,
        ')':0
    }
    output = []
    def is_operand(ch):
        return ch.isalnum()
    
    for token in expression:
        if is_operand(token):
            output.append(token)
        elif token == '(':
            s.push(token)
        elif token == ')':
            while not s.isEmpty() and s.peek() != '(':
                output.append(s.pop())
            s.pop()
        else:
            while not s.isEmpty() and precedence[s.peek()] >= precedence[token]:
                output.append(s.pop())     
            s.push(token) 

    while not s.isEmpty():
        output.append(s.pop())

    return ''.join(output)                  


s = Stack()  
exp = 'a+b*c-(d/e+f)*g'
print(infix_to_postfix(exp))