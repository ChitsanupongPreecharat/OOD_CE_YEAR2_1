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

def match(open,close):
    op = '([{'
    cl = ')]}'
    return op.index(open) == cl.index(close)

def parentMatching(str):
    
    i = 0 
    error = 0

    while i<len(str) and error == 0 :
        c = str[i]
        if c in '{[(':
            s.push(c)
        else:
            if c in '}])':
                if s.size() > 0:
                    if not match(s.pop(),c):                  
                        error = 1
                else:
                    error = 2
        i += 1
    if s.size() > 0:
        error = 3
    return error      

s = Stack()
str = '[{a+b-c}'
err = parentMatching(str)
if err == 1:
    print(str , 'unmatch open-close ')
elif err == 2:
    print(str , 'close paren excess')
elif err == 3:
    print(str , 'open paren(s) excess ', s.size(),': ',end='' )
    for ele in s.item:
        print(ele,sep=' ',end = '')
    print()
else:
    print(str, 'MATCH')                    