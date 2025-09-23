class Stack:
    def __init__(self):
        self.list = []

    def push(self,data):
        self.list.append(data)

    def pop(self):
        if not self.isEmpty():
            return self.list.pop()
    
    def peek(self):
        return self.list[-1]
    
    def isEmpty(self):
        return self.list == []
    
    def size(self):
        return len(self.list)
    
print("*****Big leg on the right side*****")
num = list(map(int,input("Enter input: ").split()))
output = [-1]*len(num)
s = Stack()
for i in range(len(num)):
    while not s.isEmpty() and num[i] > num[s.peek()]:
        most = s.pop()
        output[most] = num[i]
        print(f"input[{i}]({num[i]}) is greater than input[top of stack]({num[most]})")
        print("Stack pop")
        print(f"Output: {output}")

    s.push(i)
    print(f"Stack push {i} index of {num[i]}")
print(f"Output: {output}")