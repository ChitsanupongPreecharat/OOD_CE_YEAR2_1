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

def solution(list):
    s=Stack()
    for i in list:
        if s.isEmpty():
            s.push(i)
        elif s.peek()-i==5 or s.peek()+i==5 or s.peek()-i==10 or s.peek()+i==10:
            s.push(i)
    return s.item  
print("***Always 5 or 10***")
list = list(map(int,input("Enter Input : ").split()))

result = solution(list)
res =' '.join(map(str,result))
print("Output :",res)